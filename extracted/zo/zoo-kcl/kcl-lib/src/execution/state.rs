use std::sync::Arc;

use anyhow::Result;
use indexmap::IndexMap;
#[cfg(feature = "artifact-graph")]
use kittycad_modeling_cmds::websocket::WebSocketResponse;
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};
use uuid::Uuid;

#[cfg(feature = "artifact-graph")]
use crate::execution::{Artifact, ArtifactCommand, ArtifactGraph, ArtifactId};
use crate::{
    errors::{KclError, KclErrorDetails, Severity},
    execution::{
        annotations,
        cad_op::Operation,
        id_generator::IdGenerator,
        memory::{ProgramMemory, Stack},
        types,
        types::NumericType,
        EnvironmentRef, ExecOutcome, ExecutorSettings, KclValue, UnitAngle, UnitLen,
    },
    modules::{ModuleId, ModuleInfo, ModuleLoader, ModulePath, ModuleRepr, ModuleSource},
    parsing::ast::types::Annotation,
    source_range::SourceRange,
    CompilationError,
};

/// State for executing a program.
#[derive(Debug, Clone)]
pub struct ExecState {
    pub(super) global: GlobalState,
    pub(super) mod_local: ModuleState,
    pub(super) exec_context: Option<super::ExecutorContext>,
}

pub type ModuleInfoMap = IndexMap<ModuleId, ModuleInfo>;

#[derive(Debug, Clone)]
pub(super) struct GlobalState {
    /// Map from source file absolute path to module ID.
    pub path_to_source_id: IndexMap<ModulePath, ModuleId>,
    /// Map from module ID to source file.
    pub id_to_source: IndexMap<ModuleId, ModuleSource>,
    /// Map from module ID to module info.
    pub module_infos: ModuleInfoMap,
    /// Output map of UUIDs to artifacts.
    #[cfg(feature = "artifact-graph")]
    pub artifacts: IndexMap<ArtifactId, Artifact>,
    /// Output commands to allow building the artifact graph by the caller.
    /// These are accumulated in the [`ExecutorContext`] but moved here for
    /// convenience of the execution cache.
    #[cfg(feature = "artifact-graph")]
    pub artifact_commands: Vec<ArtifactCommand>,
    /// Responses from the engine for `artifact_commands`.  We need to cache
    /// this so that we can build the artifact graph.  These are accumulated in
    /// the [`ExecutorContext`] but moved here for convenience of the execution
    /// cache.
    #[cfg(feature = "artifact-graph")]
    pub artifact_responses: IndexMap<Uuid, WebSocketResponse>,
    /// Output artifact graph.
    #[cfg(feature = "artifact-graph")]
    pub artifact_graph: ArtifactGraph,
    /// Operations that have been performed in execution order, for display in
    /// the Feature Tree.
    #[cfg(feature = "artifact-graph")]
    pub operations: Vec<Operation>,
    /// Module loader.
    pub mod_loader: ModuleLoader,
    /// Errors and warnings.
    pub errors: Vec<CompilationError>,
}

#[derive(Debug, Clone)]
pub(super) struct ModuleState {
    /// The id generator for this module.
    pub id_generator: IdGenerator,
    pub stack: Stack,
    /// The current value of the pipe operator returned from the previous
    /// expression.  If we're not currently in a pipeline, this will be None.
    pub pipe_value: Option<KclValue>,
    /// Identifiers that have been exported from the current module.
    pub module_exports: Vec<String>,
    /// Settings specified from annotations.
    pub settings: MetaSettings,
    pub(super) explicit_length_units: bool,
    pub(super) path: ModulePath,
}

impl ExecState {
    pub fn new(exec_context: &super::ExecutorContext) -> Self {
        ExecState {
            global: GlobalState::new(&exec_context.settings),
            mod_local: ModuleState::new(ModulePath::Main, ProgramMemory::new(), Default::default()),
            exec_context: Some(exec_context.clone()),
        }
    }

    pub(super) fn reset(&mut self, exec_context: &super::ExecutorContext) {
        let global = GlobalState::new(&exec_context.settings);

        *self = ExecState {
            global,
            mod_local: ModuleState::new(self.mod_local.path.clone(), ProgramMemory::new(), Default::default()),
            exec_context: Some(exec_context.clone()),
        };
    }

    /// Log a non-fatal error.
    pub fn err(&mut self, e: CompilationError) {
        self.global.errors.push(e);
    }

    /// Log a warning.
    pub fn warn(&mut self, mut e: CompilationError) {
        e.severity = Severity::Warning;
        self.global.errors.push(e);
    }

    pub fn errors(&self) -> &[CompilationError] {
        &self.global.errors
    }

    /// Convert to execution outcome when running in WebAssembly.  We want to
    /// reduce the amount of data that crosses the WASM boundary as much as
    /// possible.
    pub async fn to_exec_outcome(self, main_ref: EnvironmentRef) -> ExecOutcome {
        // Fields are opt-in so that we don't accidentally leak private internal
        // state when we add more to ExecState.
        ExecOutcome {
            variables: self
                .stack()
                .find_all_in_env(main_ref)
                .map(|(k, v)| (k.clone(), v.clone()))
                .collect(),
            #[cfg(feature = "artifact-graph")]
            operations: self.global.operations,
            #[cfg(feature = "artifact-graph")]
            artifact_commands: self.global.artifact_commands,
            #[cfg(feature = "artifact-graph")]
            artifact_graph: self.global.artifact_graph,
            errors: self.global.errors,
            filenames: self
                .global
                .path_to_source_id
                .iter()
                .map(|(k, v)| ((*v), k.clone()))
                .collect(),
            default_planes: if let Some(ctx) = &self.exec_context {
                ctx.engine.get_default_planes().read().await.clone()
            } else {
                None
            },
        }
    }

    pub async fn to_mock_exec_outcome(self, main_ref: EnvironmentRef) -> ExecOutcome {
        // Fields are opt-in so that we don't accidentally leak private internal
        // state when we add more to ExecState.
        ExecOutcome {
            variables: self
                .stack()
                .find_all_in_env(main_ref)
                .map(|(k, v)| (k.clone(), v.clone()))
                .collect(),
            #[cfg(feature = "artifact-graph")]
            operations: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifact_commands: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifact_graph: Default::default(),
            errors: self.global.errors,
            filenames: Default::default(),
            default_planes: if let Some(ctx) = &self.exec_context {
                ctx.engine.get_default_planes().read().await.clone()
            } else {
                None
            },
        }
    }

    pub(crate) fn stack(&self) -> &Stack {
        &self.mod_local.stack
    }

    pub(crate) fn mut_stack(&mut self) -> &mut Stack {
        &mut self.mod_local.stack
    }

    pub fn next_uuid(&mut self) -> Uuid {
        self.mod_local.id_generator.next_uuid()
    }

    pub fn id_generator(&mut self) -> &mut IdGenerator {
        &mut self.mod_local.id_generator
    }

    #[cfg(feature = "artifact-graph")]
    pub(crate) fn add_artifact(&mut self, artifact: Artifact) {
        let id = artifact.id();
        self.global.artifacts.insert(id, artifact);
    }

    pub(crate) fn push_op(&mut self, op: Operation) {
        #[cfg(feature = "artifact-graph")]
        self.global.operations.push(op);
        #[cfg(not(feature = "artifact-graph"))]
        drop(op);
    }

    pub(super) fn next_module_id(&self) -> ModuleId {
        ModuleId::from_usize(self.global.path_to_source_id.len())
    }

    pub(super) fn id_for_module(&self, path: &ModulePath) -> Option<ModuleId> {
        self.global.path_to_source_id.get(path).cloned()
    }

    pub(super) fn add_path_to_source_id(&mut self, path: ModulePath, id: ModuleId) {
        debug_assert!(!self.global.path_to_source_id.contains_key(&path));
        self.global.path_to_source_id.insert(path.clone(), id);
    }

    pub(crate) fn add_root_module_contents(&mut self, program: &crate::Program) {
        let root_id = ModuleId::default();
        // Get the path for the root module.
        let path = self
            .global
            .path_to_source_id
            .iter()
            .find(|(_, v)| **v == root_id)
            .unwrap()
            .0
            .clone();
        self.add_id_to_source(
            root_id,
            ModuleSource {
                path,
                source: program.original_file_contents.to_string(),
            },
        );
    }

    pub(super) fn add_id_to_source(&mut self, id: ModuleId, source: ModuleSource) {
        self.global.id_to_source.insert(id, source.clone());
    }

    pub(super) fn get_source(&self, id: ModuleId) -> Option<&ModuleSource> {
        self.global.id_to_source.get(&id)
    }

    pub(super) fn add_module(&mut self, id: ModuleId, path: ModulePath, repr: ModuleRepr) {
        debug_assert!(self.global.path_to_source_id.contains_key(&path));
        let module_info = ModuleInfo { id, repr, path };
        self.global.module_infos.insert(id, module_info);
    }

    pub fn get_module(&mut self, id: ModuleId) -> Option<&ModuleInfo> {
        self.global.module_infos.get(&id)
    }

    pub fn current_default_units(&self) -> NumericType {
        NumericType::Default {
            len: self.length_unit(),
            angle: self.angle_unit(),
        }
    }

    pub fn length_unit(&self) -> UnitLen {
        self.mod_local.settings.default_length_units
    }

    pub fn angle_unit(&self) -> UnitAngle {
        self.mod_local.settings.default_angle_units
    }

    pub(super) fn circular_import_error(&self, path: &ModulePath, source_range: SourceRange) -> KclError {
        KclError::ImportCycle(KclErrorDetails::new(
            format!(
                "circular import of modules is not allowed: {} -> {}",
                self.global
                    .mod_loader
                    .import_stack
                    .iter()
                    .map(|p| p.to_string_lossy())
                    .collect::<Vec<_>>()
                    .join(" -> "),
                path,
            ),
            vec![source_range],
        ))
    }

    pub(crate) fn pipe_value(&self) -> Option<&KclValue> {
        self.mod_local.pipe_value.as_ref()
    }
}

impl GlobalState {
    fn new(settings: &ExecutorSettings) -> Self {
        let mut global = GlobalState {
            path_to_source_id: Default::default(),
            module_infos: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifacts: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifact_commands: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifact_responses: Default::default(),
            #[cfg(feature = "artifact-graph")]
            artifact_graph: Default::default(),
            #[cfg(feature = "artifact-graph")]
            operations: Default::default(),
            mod_loader: Default::default(),
            errors: Default::default(),
            id_to_source: Default::default(),
        };

        let root_id = ModuleId::default();
        let root_path = settings.current_file.clone().unwrap_or_default();
        global.module_infos.insert(
            root_id,
            ModuleInfo {
                id: root_id,
                path: ModulePath::Local {
                    value: root_path.clone(),
                },
                repr: ModuleRepr::Root,
            },
        );
        global
            .path_to_source_id
            .insert(ModulePath::Local { value: root_path }, root_id);
        global
    }
}

impl ModuleState {
    pub(super) fn new(path: ModulePath, memory: Arc<ProgramMemory>, module_id: Option<ModuleId>) -> Self {
        ModuleState {
            id_generator: IdGenerator::new(module_id),
            stack: memory.new_stack(),
            pipe_value: Default::default(),
            module_exports: Default::default(),
            explicit_length_units: false,
            path,
            settings: MetaSettings {
                default_length_units: Default::default(),
                default_angle_units: Default::default(),
                kcl_version: "0.1".to_owned(),
            },
        }
    }
}

#[derive(Debug, Default, Clone, Deserialize, Serialize, PartialEq, Eq, ts_rs::TS, JsonSchema)]
#[ts(export)]
#[serde(rename_all = "camelCase")]
pub struct MetaSettings {
    pub default_length_units: types::UnitLen,
    pub default_angle_units: types::UnitAngle,
    pub kcl_version: String,
}

impl MetaSettings {
    pub(crate) fn update_from_annotation(
        &mut self,
        annotation: &crate::parsing::ast::types::Node<Annotation>,
    ) -> Result<bool, KclError> {
        let properties = annotations::expect_properties(annotations::SETTINGS, annotation)?;

        let mut updated_len = false;
        for p in properties {
            match &*p.inner.key.name {
                annotations::SETTINGS_UNIT_LENGTH => {
                    let value = annotations::expect_ident(&p.inner.value)?;
                    let value = types::UnitLen::from_str(value, annotation.as_source_range())?;
                    self.default_length_units = value;
                    updated_len = true;
                }
                annotations::SETTINGS_UNIT_ANGLE => {
                    let value = annotations::expect_ident(&p.inner.value)?;
                    let value = types::UnitAngle::from_str(value, annotation.as_source_range())?;
                    self.default_angle_units = value;
                }
                annotations::SETTINGS_VERSION => {
                    let value = annotations::expect_number(&p.inner.value)?;
                    self.kcl_version = value;
                }
                name => {
                    return Err(KclError::Semantic(KclErrorDetails::new(
                        format!(
                            "Unexpected settings key: `{name}`; expected one of `{}`, `{}`",
                            annotations::SETTINGS_UNIT_LENGTH,
                            annotations::SETTINGS_UNIT_ANGLE
                        ),
                        vec![annotation.as_source_range()],
                    )))
                }
            }
        }

        Ok(updated_len)
    }
}
