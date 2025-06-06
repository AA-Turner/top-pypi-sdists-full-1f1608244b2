use darling::{Error, FromMeta, Result, ast::NestedMeta};
use proc_macro2::TokenStream;
use std::{collections::HashMap, str::FromStr};
use syn::{Expr, ExprLit, Lit, Meta, MetaNameValue, Token, Type, punctuated::Punctuated};

use crate::{TypeRecipe, Value};

use super::signature::{syn_path_to_string, syn_type_to_type_recipe};

// Arguments to the bootstrap proc-macro
// The rest of this file is for parsing the arguments to bootstrap(*) into the Bootstrap struct
#[derive(Debug, FromMeta, Clone)]
pub struct BootstrapArguments {
    pub name: Option<String>,
    pub proof_path: Option<String>,
    #[darling(default)]
    pub has_ffi: Option<bool>,
    #[darling(default)]
    pub unproven: bool,
    #[darling(default)]
    pub features: Features,
    #[darling(default)]
    pub generics: BootTypeHashMap,
    #[darling(default)]
    pub arguments: BootTypeHashMap,
    pub derived_types: Option<DerivedTypes>,
    pub returns: Option<BootType>,
}

impl BootstrapArguments {
    pub fn from_attribute_args(items: &[NestedMeta]) -> darling::Result<Self> {
        Self::from_list(items)
    }
}

#[derive(Debug, Clone, Default)]
pub struct DerivedTypes(pub Vec<(String, TypeRecipe)>);

impl FromMeta for DerivedTypes {
    fn from_list(items: &[NestedMeta]) -> Result<Self> {
        // each item should be a metalist consisting of the derived type name and info: T = "X"

        (items.iter())
            .map(|nested| {
                let NestedMeta::Meta(Meta::NameValue(MetaNameValue { path, value, .. })) = nested
                else {
                    return Err(
                        Error::custom("expected name = value pairs in derived_types")
                            .with_span(nested),
                    );
                };
                let Expr::Lit(ExprLit { lit, .. }) = value else {
                    return Err(Error::custom("expected literal").with_span(value));
                };
                Ok((syn_path_to_string(path)?, TypeRecipe::from_value(lit)?))
            })
            .collect::<Result<Vec<(String, TypeRecipe)>>>()
            .map(DerivedTypes)
    }
}

#[derive(Debug, Clone, Default)]
pub struct Features(pub Vec<String>);

impl FromMeta for Features {
    fn from_list(items: &[NestedMeta]) -> darling::Result<Self> {
        items
            .iter()
            .map(String::from_nested_meta)
            .collect::<darling::Result<Vec<String>>>()
            .map(Features)
    }
}

#[derive(Debug, Clone, Default)]
pub struct BootTypeHashMap(pub HashMap<String, BootType>);

impl FromMeta for BootTypeHashMap {
    fn from_list(items: &[NestedMeta]) -> darling::Result<Self> {
        (items.iter())
            .map(|nested| {
                if let NestedMeta::Meta(Meta::List(list)) = nested {
                    let type_name = list
                        .path
                        .get_ident()
                        .ok_or_else(|| {
                            darling::Error::custom("path must consist of a single ident")
                                .with_span(&list.path)
                        })?
                        .to_string();

                    let type_ = BootType::from_list(
                        &list
                            .parse_args_with(Punctuated::<NestedMeta, Token![,]>::parse_terminated)?
                            .into_iter()
                            .collect::<Vec<_>>(),
                    )?;
                    Ok((type_name, type_))
                } else {
                    Err(
                        darling::Error::custom("expected metalist in BootstrapTypes")
                            .with_span(nested),
                    )
                }
            })
            .collect::<darling::Result<HashMap<String, BootType>>>()
            .map(BootTypeHashMap)
    }
}

#[derive(Debug, FromMeta, Clone, Default)]
pub struct BootType {
    pub c_type: Option<String>,
    pub rust_type: Option<TypeRecipe>,
    pub hint: Option<String>,
    pub default: Option<Value>,
    #[darling(default)]
    pub do_not_convert: bool,
    pub example: Option<TypeRecipe>,
    #[darling(default)]
    pub suppress: bool,
}

impl FromMeta for Value {
    fn from_expr(expr: &Expr) -> Result<Self> {
        match *expr {
            Expr::Unary(ref unary) => {
                if !matches!(unary.op, syn::UnOp::Neg(_)) {
                    return Err(
                        Error::custom("the only unary operation supported is negation")
                            .with_span(expr),
                    );
                }
                Ok(match Self::from_expr(&unary.expr)? {
                    Value::Integer(v) => Value::Integer(-v),
                    Value::Float(v) => Value::Float(-v),
                    v => v,
                })
            }
            Expr::Lit(ref lit) => Self::from_value(&lit.lit),
            Expr::Group(ref group) => {
                // syn may generate this invisible group delimiter when the input to the darling
                // proc macro (specifically, the attributes) are generated by a
                // macro_rules! (e.g. propagating a macro_rules!'s expr)
                // Since we want to basically ignore these invisible group delimiters,
                // we just propagate the call to the inner expression.
                Self::from_expr(&group.expr)
            }
            _ => Err(Error::unexpected_expr_type(expr)),
        }
        .map_err(|e| e.with_span(expr))
    }

    fn from_value(value: &syn::Lit) -> darling::Result<Self> {
        Ok(match value {
            syn::Lit::Str(str) => Value::String(str.value()),
            syn::Lit::Int(int) => Value::Integer(int.base10_parse::<i64>()?),
            syn::Lit::Float(float) => Value::Float(float.base10_parse::<f64>()?),
            syn::Lit::Bool(bool) => Value::Bool(bool.value),
            syn::Lit::ByteStr(bstr) => {
                if bstr.value() == b"null" {
                    Value::Null
                } else {
                    return Err(Error::custom("Byte strings are reserved for expressing nullity. Use b\"null\" to represent a null literal.").with_span(bstr));
                }
            }
            lit => return Err(darling::Error::unexpected_lit_type(lit).with_span(value)),
        })
    }
}

impl FromMeta for TypeRecipe {
    fn from_value(value: &Lit) -> Result<Self> {
        match value {
            Lit::Str(litstr) => {
                let litstr = litstr.value();
                if litstr.starts_with('$') {
                    let mut chars = litstr.chars();
                    chars.next(); // discard leading $
                    let stream = TokenStream::from_str(chars.as_str()).map_err(|_| {
                        Error::custom("error while lexing function").with_span(value)
                    })?;

                    syn_meta_to_type_recipe_function(syn::parse2::<NestedMeta>(stream)?)
                } else {
                    let stream = TokenStream::from_str(&litstr)
                        .map_err(|_| Error::custom("error while lexing type").with_span(value))?;

                    let ty = syn::parse2::<Type>(stream).map_err(|e| {
                        Error::custom(format!(
                            "error while parsing type {}: {}",
                            litstr,
                            e.to_string()
                        ))
                        .with_span(value)
                    })?;
                    syn_type_to_type_recipe(&ty)
                }
            }
            Lit::ByteStr(bstr) => {
                if bstr.value() == b"null" {
                    Ok(TypeRecipe::None)
                } else {
                    Err(Error::custom("Byte strings are reserved for expressing nullity. Use b\"null\" to represent a null literal.").with_span(bstr))
                }
            }
            _ => Err(Error::custom("expected string").with_span(value)),
        }
    }
}

fn syn_meta_to_type_recipe_function(meta: NestedMeta) -> Result<TypeRecipe> {
    match meta {
        NestedMeta::Meta(Meta::Path(path)) => syn_path_to_string(&path).map(TypeRecipe::Name),
        NestedMeta::Meta(Meta::List(list)) => Ok(TypeRecipe::Function {
            function: syn_path_to_string(&list.path)?,
            params: list
                .parse_args_with(Punctuated::<NestedMeta, Token![,]>::parse_terminated)?
                .into_iter()
                .map(syn_meta_to_type_recipe_function)
                .collect::<Result<Vec<TypeRecipe>>>()?,
        }),
        meta => Err(Error::custom(
            "rust_type = \"$<expression>\" only supports a limited function grammar",
        )
        .with_span(&meta)),
    }
}

#[derive(Debug, Default, Clone)]
pub struct DefaultGenerics(pub Vec<String>);

impl FromMeta for DefaultGenerics {
    fn from_value(lit: &Lit) -> Result<Self> {
        if let Lit::Str(litstr) = lit {
            Ok(DefaultGenerics(
                litstr
                    .value()
                    .split(',')
                    .map(|v| v.trim().to_string())
                    .collect(),
            ))
        } else {
            Err(Error::custom("expected string").with_span(lit))
        }
    }
}
