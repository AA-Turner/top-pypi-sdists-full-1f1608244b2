# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class Meta(TeaModel):
    def __init__(
        self,
        active: bool = None,
        alias: str = None,
        category: str = None,
        code: str = None,
        force_active: bool = None,
        force_required: bool = None,
        required: bool = None,
        scheme: Dict[str, Any] = None,
        title: str = None,
        type: str = None,
    ):
        self.active = active
        self.alias = alias
        self.category = category
        self.code = code
        self.force_active = force_active
        self.force_required = force_required
        self.required = required
        self.scheme = scheme
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.alias is not None:
            result['alias'] = self.alias
        if self.category is not None:
            result['category'] = self.category
        if self.code is not None:
            result['code'] = self.code
        if self.force_active is not None:
            result['forceActive'] = self.force_active
        if self.force_required is not None:
            result['forceRequired'] = self.force_required
        if self.required is not None:
            result['required'] = self.required
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('forceActive') is not None:
            self.force_active = m.get('forceActive')
        if m.get('forceRequired') is not None:
            self.force_required = m.get('forceRequired')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class EntityChildren(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        id: str = None,
        is_deleted: str = None,
        link_source_id: str = None,
        link_source_type: str = None,
        metas: List[Meta] = None,
        type: str = None,
    ):
        self.data = data
        self.id = id
        self.is_deleted = is_deleted
        self.link_source_id = link_source_id
        self.link_source_type = link_source_type
        self.metas = metas
        self.type = type

    def validate(self):
        if self.metas:
            for k in self.metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.id is not None:
            result['id'] = self.id
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.link_source_id is not None:
            result['linkSourceId'] = self.link_source_id
        if self.link_source_type is not None:
            result['linkSourceType'] = self.link_source_type
        result['metas'] = []
        if self.metas is not None:
            for k in self.metas:
                result['metas'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('linkSourceId') is not None:
            self.link_source_id = m.get('linkSourceId')
        if m.get('linkSourceType') is not None:
            self.link_source_type = m.get('linkSourceType')
        self.metas = []
        if m.get('metas') is not None:
            for k in m.get('metas'):
                temp_model = Meta()
                self.metas.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Entity(TeaModel):
    def __init__(
        self,
        children: List[EntityChildren] = None,
        data: Dict[str, Any] = None,
        id: str = None,
        is_deleted: str = None,
        link_source_id: str = None,
        link_source_type: str = None,
        metas: List[Meta] = None,
        type: str = None,
    ):
        self.children = children
        self.data = data
        self.id = id
        self.is_deleted = is_deleted
        self.link_source_id = link_source_id
        self.link_source_type = link_source_type
        self.metas = metas
        self.type = type

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.metas:
            for k in self.metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['children'] = []
        if self.children is not None:
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        if self.data is not None:
            result['data'] = self.data
        if self.id is not None:
            result['id'] = self.id
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.link_source_id is not None:
            result['linkSourceId'] = self.link_source_id
        if self.link_source_type is not None:
            result['linkSourceType'] = self.link_source_type
        result['metas'] = []
        if self.metas is not None:
            for k in self.metas:
                result['metas'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k in m.get('children'):
                temp_model = EntityChildren()
                self.children.append(temp_model.from_map(k))
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('linkSourceId') is not None:
            self.link_source_id = m.get('linkSourceId')
        if m.get('linkSourceType') is not None:
            self.link_source_type = m.get('linkSourceType')
        self.metas = []
        if m.get('metas') is not None:
            for k in m.get('metas'):
                temp_model = Meta()
                self.metas.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OpenAgoalAlignDTO(TeaModel):
    def __init__(
        self,
        align_type: str = None,
        object_id: str = None,
        object_type: str = None,
        objective_id: str = None,
    ):
        # This parameter is required.
        self.align_type = align_type
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.object_type = object_type
        # This parameter is required.
        self.objective_id = objective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align_type is not None:
            result['alignType'] = self.align_type
        if self.object_id is not None:
            result['objectId'] = self.object_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignType') is not None:
            self.align_type = m.get('alignType')
        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        return self


class OpenAgoalFieldMetaDTO(TeaModel):
    def __init__(
        self,
        active: bool = None,
        alias: str = None,
        code: str = None,
        entity_type: str = None,
        field_id: str = None,
        note: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
    ):
        # 是否启用
        # 
        # This parameter is required.
        self.active = active
        # 字段元数据别名
        self.alias = alias
        # 字段元数据标识
        # 
        # This parameter is required.
        self.code = code
        # 实体类型
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # 字段ID
        # 
        # This parameter is required.
        self.field_id = field_id
        # 字段备注
        self.note = note
        # 字段数据来源
        # 
        # This parameter is required.
        self.source = source
        # 字段元数据名称
        # 
        # This parameter is required.
        self.title = title
        # 字段类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.alias is not None:
            result['alias'] = self.alias
        if self.code is not None:
            result['code'] = self.code
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.note is not None:
            result['note'] = self.note
        if self.source is not None:
            result['source'] = self.source
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('note') is not None:
            self.note = m.get('note')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OpenAgoalKeyActionDTO(TeaModel):
    def __init__(
        self,
        key_action_id: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.key_action_id = key_action_id
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_action_id is not None:
            result['keyActionId'] = self.key_action_id
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyActionId') is not None:
            self.key_action_id = m.get('keyActionId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class OpenAgoalUserDTO(TeaModel):
    def __init__(
        self,
        ding_user_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.ding_user_id = ding_user_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_user_id is not None:
            result['dingUserId'] = self.ding_user_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingUserId') is not None:
            self.ding_user_id = m.get('dingUserId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class TitleMention(TeaModel):
    def __init__(
        self,
        length: int = None,
        offset: int = None,
        user: OpenAgoalUserDTO = None,
    ):
        # This parameter is required.
        self.length = length
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['length'] = self.length
        if self.offset is not None:
            result['offset'] = self.offset
        if self.user is not None:
            result['user'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('length') is not None:
            self.length = m.get('length')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('user') is not None:
            temp_model = OpenAgoalUserDTO()
            self.user = temp_model.from_map(m['user'])
        return self


class OpenAgoalKeyResultDTO(TeaModel):
    def __init__(
        self,
        key_actions: List[OpenAgoalKeyActionDTO] = None,
        key_result_id: str = None,
        progress: int = None,
        status: int = None,
        title: str = None,
        title_mentions: List[TitleMention] = None,
        type: int = None,
        weight: float = None,
    ):
        # This parameter is required.
        self.key_actions = key_actions
        # This parameter is required.
        self.key_result_id = key_result_id
        # This parameter is required.
        self.progress = progress
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.title_mentions = title_mentions
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.weight = weight

    def validate(self):
        if self.key_actions:
            for k in self.key_actions:
                if k:
                    k.validate()
        if self.title_mentions:
            for k in self.title_mentions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keyActions'] = []
        if self.key_actions is not None:
            for k in self.key_actions:
                result['keyActions'].append(k.to_map() if k else None)
        if self.key_result_id is not None:
            result['keyResultId'] = self.key_result_id
        if self.progress is not None:
            result['progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        if self.title is not None:
            result['title'] = self.title
        result['titleMentions'] = []
        if self.title_mentions is not None:
            for k in self.title_mentions:
                result['titleMentions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_actions = []
        if m.get('keyActions') is not None:
            for k in m.get('keyActions'):
                temp_model = OpenAgoalKeyActionDTO()
                self.key_actions.append(temp_model.from_map(k))
        if m.get('keyResultId') is not None:
            self.key_result_id = m.get('keyResultId')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('title') is not None:
            self.title = m.get('title')
        self.title_mentions = []
        if m.get('titleMentions') is not None:
            for k in m.get('titleMentions'):
                temp_model = TitleMention()
                self.title_mentions.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class OpenAgoalLatestProgressDTO(TeaModel):
    def __init__(
        self,
        created: int = None,
        creator: OpenAgoalUserDTO = None,
        htmldescription: str = None,
        progress_id: str = None,
    ):
        # This parameter is required.
        self.created = created
        # This parameter is required.
        self.creator = creator
        # This parameter is required.
        self.htmldescription = htmldescription
        # This parameter is required.
        self.progress_id = progress_id

    def validate(self):
        if self.creator:
            self.creator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.creator is not None:
            result['creator'] = self.creator.to_map()
        if self.htmldescription is not None:
            result['htmldescription'] = self.htmldescription
        if self.progress_id is not None:
            result['progressId'] = self.progress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('creator') is not None:
            temp_model = OpenAgoalUserDTO()
            self.creator = temp_model.from_map(m['creator'])
        if m.get('htmldescription') is not None:
            self.htmldescription = m.get('htmldescription')
        if m.get('progressId') is not None:
            self.progress_id = m.get('progressId')
        return self


class OpenOrgObjectiveRuleDTO(TeaModel):
    def __init__(
        self,
        objective_category: str = None,
        objective_rule_id: str = None,
        objective_rule_name: str = None,
    ):
        # This parameter is required.
        self.objective_category = objective_category
        # This parameter is required.
        self.objective_rule_id = objective_rule_id
        # This parameter is required.
        self.objective_rule_name = objective_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_category is not None:
            result['objectiveCategory'] = self.objective_category
        if self.objective_rule_id is not None:
            result['objectiveRuleId'] = self.objective_rule_id
        if self.objective_rule_name is not None:
            result['objectiveRuleName'] = self.objective_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveCategory') is not None:
            self.objective_category = m.get('objectiveCategory')
        if m.get('objectiveRuleId') is not None:
            self.objective_rule_id = m.get('objectiveRuleId')
        if m.get('objectiveRuleName') is not None:
            self.objective_rule_name = m.get('objectiveRuleName')
        return self


class OpenObjectiveRulePeriodDTO(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        name: str = None,
        period_id: str = None,
        period_type: str = None,
        start_date: int = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.period_id = period_id
        # This parameter is required.
        self.period_type = period_type
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.name is not None:
            result['name'] = self.name
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.start_date is not None:
            result['startDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        return self


class OpenAgoalTeamDTO(TeaModel):
    def __init__(
        self,
        dept_id: str = None,
        name: str = None,
        team_id: str = None,
    ):
        # This parameter is required.
        self.dept_id = dept_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.team_id = team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.name is not None:
            result['name'] = self.name
        if self.team_id is not None:
            result['teamId'] = self.team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')
        return self


class OpenAgoalObjectiveDTO(TeaModel):
    def __init__(
        self,
        executor: OpenAgoalUserDTO = None,
        key_actions: List[OpenAgoalKeyActionDTO] = None,
        key_results: List[OpenAgoalKeyResultDTO] = None,
        latest_progress: OpenAgoalLatestProgressDTO = None,
        objective_id: str = None,
        objective_rule: OpenOrgObjectiveRuleDTO = None,
        period: OpenObjectiveRulePeriodDTO = None,
        progress: int = None,
        status: int = None,
        teams: List[OpenAgoalTeamDTO] = None,
        title: str = None,
        weight: float = None,
    ):
        # This parameter is required.
        self.executor = executor
        # This parameter is required.
        self.key_actions = key_actions
        # This parameter is required.
        self.key_results = key_results
        # This parameter is required.
        self.latest_progress = latest_progress
        # This parameter is required.
        self.objective_id = objective_id
        # This parameter is required.
        self.objective_rule = objective_rule
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.progress = progress
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.teams = teams
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.weight = weight

    def validate(self):
        if self.executor:
            self.executor.validate()
        if self.key_actions:
            for k in self.key_actions:
                if k:
                    k.validate()
        if self.key_results:
            for k in self.key_results:
                if k:
                    k.validate()
        if self.latest_progress:
            self.latest_progress.validate()
        if self.objective_rule:
            self.objective_rule.validate()
        if self.period:
            self.period.validate()
        if self.teams:
            for k in self.teams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor is not None:
            result['executor'] = self.executor.to_map()
        result['keyActions'] = []
        if self.key_actions is not None:
            for k in self.key_actions:
                result['keyActions'].append(k.to_map() if k else None)
        result['keyResults'] = []
        if self.key_results is not None:
            for k in self.key_results:
                result['keyResults'].append(k.to_map() if k else None)
        if self.latest_progress is not None:
            result['latestProgress'] = self.latest_progress.to_map()
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.objective_rule is not None:
            result['objectiveRule'] = self.objective_rule.to_map()
        if self.period is not None:
            result['period'] = self.period.to_map()
        if self.progress is not None:
            result['progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        result['teams'] = []
        if self.teams is not None:
            for k in self.teams:
                result['teams'].append(k.to_map() if k else None)
        if self.title is not None:
            result['title'] = self.title
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executor') is not None:
            temp_model = OpenAgoalUserDTO()
            self.executor = temp_model.from_map(m['executor'])
        self.key_actions = []
        if m.get('keyActions') is not None:
            for k in m.get('keyActions'):
                temp_model = OpenAgoalKeyActionDTO()
                self.key_actions.append(temp_model.from_map(k))
        self.key_results = []
        if m.get('keyResults') is not None:
            for k in m.get('keyResults'):
                temp_model = OpenAgoalKeyResultDTO()
                self.key_results.append(temp_model.from_map(k))
        if m.get('latestProgress') is not None:
            temp_model = OpenAgoalLatestProgressDTO()
            self.latest_progress = temp_model.from_map(m['latestProgress'])
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('objectiveRule') is not None:
            temp_model = OpenOrgObjectiveRuleDTO()
            self.objective_rule = temp_model.from_map(m['objectiveRule'])
        if m.get('period') is not None:
            temp_model = OpenObjectiveRulePeriodDTO()
            self.period = temp_model.from_map(m['period'])
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.teams = []
        if m.get('teams') is not None:
            for k in m.get('teams'):
                temp_model = OpenAgoalTeamDTO()
                self.teams.append(temp_model.from_map(k))
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class OpenAgoalObjectiveDimensionDTO(TeaModel):
    def __init__(
        self,
        children: List['OpenAgoalObjectiveDimensionDTO'] = None,
        dimension_id: str = None,
        field_config: List[OpenAgoalFieldMetaDTO] = None,
        field_value_map: Dict[str, Any] = None,
        title: str = None,
        weight: float = None,
    ):
        # This parameter is required.
        self.children = children
        # This parameter is required.
        self.dimension_id = dimension_id
        # This parameter is required.
        self.field_config = field_config
        # This parameter is required.
        self.field_value_map = field_value_map
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.weight = weight

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.field_config:
            for k in self.field_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['children'] = []
        if self.children is not None:
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        if self.dimension_id is not None:
            result['dimensionId'] = self.dimension_id
        result['fieldConfig'] = []
        if self.field_config is not None:
            for k in self.field_config:
                result['fieldConfig'].append(k.to_map() if k else None)
        if self.field_value_map is not None:
            result['fieldValueMap'] = self.field_value_map
        if self.title is not None:
            result['title'] = self.title
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k in m.get('children'):
                temp_model = OpenAgoalObjectiveDimensionDTO()
                self.children.append(temp_model.from_map(k))
        if m.get('dimensionId') is not None:
            self.dimension_id = m.get('dimensionId')
        self.field_config = []
        if m.get('fieldConfig') is not None:
            for k in m.get('fieldConfig'):
                temp_model = OpenAgoalFieldMetaDTO()
                self.field_config.append(temp_model.from_map(k))
        if m.get('fieldValueMap') is not None:
            self.field_value_map = m.get('fieldValueMap')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class OpenAgoalOrgObjectiveDTO(TeaModel):
    def __init__(
        self,
        dimension: OpenAgoalObjectiveDimensionDTO = None,
        down_align_objects: List[OpenAgoalAlignDTO] = None,
        executor: OpenAgoalUserDTO = None,
        field_config: List[OpenAgoalFieldMetaDTO] = None,
        field_value_map: Dict[str, Any] = None,
        objective_id: str = None,
        period: OpenObjectiveRulePeriodDTO = None,
        status: str = None,
        team: OpenAgoalTeamDTO = None,
        title: str = None,
        up_align_objects: List[OpenAgoalAlignDTO] = None,
    ):
        # This parameter is required.
        self.dimension = dimension
        # This parameter is required.
        self.down_align_objects = down_align_objects
        # This parameter is required.
        self.executor = executor
        # This parameter is required.
        self.field_config = field_config
        # This parameter is required.
        self.field_value_map = field_value_map
        # This parameter is required.
        self.objective_id = objective_id
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.team = team
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.up_align_objects = up_align_objects

    def validate(self):
        if self.dimension:
            self.dimension.validate()
        if self.down_align_objects:
            for k in self.down_align_objects:
                if k:
                    k.validate()
        if self.executor:
            self.executor.validate()
        if self.field_config:
            for k in self.field_config:
                if k:
                    k.validate()
        if self.period:
            self.period.validate()
        if self.team:
            self.team.validate()
        if self.up_align_objects:
            for k in self.up_align_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['dimension'] = self.dimension.to_map()
        result['downAlignObjects'] = []
        if self.down_align_objects is not None:
            for k in self.down_align_objects:
                result['downAlignObjects'].append(k.to_map() if k else None)
        if self.executor is not None:
            result['executor'] = self.executor.to_map()
        result['fieldConfig'] = []
        if self.field_config is not None:
            for k in self.field_config:
                result['fieldConfig'].append(k.to_map() if k else None)
        if self.field_value_map is not None:
            result['fieldValueMap'] = self.field_value_map
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.period is not None:
            result['period'] = self.period.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.team is not None:
            result['team'] = self.team.to_map()
        if self.title is not None:
            result['title'] = self.title
        result['upAlignObjects'] = []
        if self.up_align_objects is not None:
            for k in self.up_align_objects:
                result['upAlignObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimension') is not None:
            temp_model = OpenAgoalObjectiveDimensionDTO()
            self.dimension = temp_model.from_map(m['dimension'])
        self.down_align_objects = []
        if m.get('downAlignObjects') is not None:
            for k in m.get('downAlignObjects'):
                temp_model = OpenAgoalAlignDTO()
                self.down_align_objects.append(temp_model.from_map(k))
        if m.get('executor') is not None:
            temp_model = OpenAgoalUserDTO()
            self.executor = temp_model.from_map(m['executor'])
        self.field_config = []
        if m.get('fieldConfig') is not None:
            for k in m.get('fieldConfig'):
                temp_model = OpenAgoalFieldMetaDTO()
                self.field_config.append(temp_model.from_map(k))
        if m.get('fieldValueMap') is not None:
            self.field_value_map = m.get('fieldValueMap')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('period') is not None:
            temp_model = OpenObjectiveRulePeriodDTO()
            self.period = temp_model.from_map(m['period'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('team') is not None:
            temp_model = OpenAgoalTeamDTO()
            self.team = temp_model.from_map(m['team'])
        if m.get('title') is not None:
            self.title = m.get('title')
        self.up_align_objects = []
        if m.get('upAlignObjects') is not None:
            for k in m.get('upAlignObjects'):
                temp_model = OpenAgoalAlignDTO()
                self.up_align_objects.append(temp_model.from_map(k))
        return self


class OpenAgoalOrgObjectiveListDTO(TeaModel):
    def __init__(
        self,
        objective_list: List[OpenAgoalOrgObjectiveDTO] = None,
        total_count: int = None,
    ):
        # This parameter is required.
        self.objective_list = objective_list
        # This parameter is required.
        self.total_count = total_count

    def validate(self):
        if self.objective_list:
            for k in self.objective_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectiveList'] = []
        if self.objective_list is not None:
            for k in self.objective_list:
                result['objectiveList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.objective_list = []
        if m.get('objectiveList') is not None:
            for k in m.get('objectiveList'):
                temp_model = OpenAgoalOrgObjectiveDTO()
                self.objective_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class OpenAgoalPeriodDTO(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        name: str = None,
        period_id: str = None,
        period_type: str = None,
        start_date: int = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.period_id = period_id
        # This parameter is required.
        self.period_type = period_type
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.name is not None:
            result['name'] = self.name
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.start_date is not None:
            result['startDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        return self


class OpenAgoalProgressDTO(TeaModel):
    def __init__(
        self,
        created: int = None,
        creator: OpenAgoalUserDTO = None,
        html_content: str = None,
        modifier: OpenAgoalUserDTO = None,
        progress_id: str = None,
        updated: int = None,
    ):
        # This parameter is required.
        self.created = created
        # This parameter is required.
        self.creator = creator
        # This parameter is required.
        self.html_content = html_content
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.progress_id = progress_id
        # This parameter is required.
        self.updated = updated

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.creator is not None:
            result['creator'] = self.creator.to_map()
        if self.html_content is not None:
            result['htmlContent'] = self.html_content
        if self.modifier is not None:
            result['modifier'] = self.modifier.to_map()
        if self.progress_id is not None:
            result['progressId'] = self.progress_id
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('creator') is not None:
            temp_model = OpenAgoalUserDTO()
            self.creator = temp_model.from_map(m['creator'])
        if m.get('htmlContent') is not None:
            self.html_content = m.get('htmlContent')
        if m.get('modifier') is not None:
            temp_model = OpenAgoalUserDTO()
            self.modifier = temp_model.from_map(m['modifier'])
        if m.get('progressId') is not None:
            self.progress_id = m.get('progressId')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class OpenUserAdminDTO(TeaModel):
    def __init__(
        self,
        ding_corp_id: str = None,
        ding_user_id: str = None,
    ):
        # This parameter is required.
        self.ding_corp_id = ding_corp_id
        # This parameter is required.
        self.ding_user_id = ding_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_corp_id is not None:
            result['dingCorpId'] = self.ding_corp_id
        if self.ding_user_id is not None:
            result['dingUserId'] = self.ding_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingCorpId') is not None:
            self.ding_corp_id = m.get('dingCorpId')
        if m.get('dingUserId') is not None:
            self.ding_user_id = m.get('dingUserId')
        return self


class OpenUserSubAdminDTO(TeaModel):
    def __init__(
        self,
        dept_ids: List[str] = None,
        ding_corp_id: str = None,
        ding_user_id: str = None,
        permission_group_codes: List[str] = None,
    ):
        # This parameter is required.
        self.dept_ids = dept_ids
        # This parameter is required.
        self.ding_corp_id = ding_corp_id
        # This parameter is required.
        self.ding_user_id = ding_user_id
        # This parameter is required.
        self.permission_group_codes = permission_group_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.ding_corp_id is not None:
            result['dingCorpId'] = self.ding_corp_id
        if self.ding_user_id is not None:
            result['dingUserId'] = self.ding_user_id
        if self.permission_group_codes is not None:
            result['permissionGroupCodes'] = self.permission_group_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('dingCorpId') is not None:
            self.ding_corp_id = m.get('dingCorpId')
        if m.get('dingUserId') is not None:
            self.ding_user_id = m.get('dingUserId')
        if m.get('permissionGroupCodes') is not None:
            self.permission_group_codes = m.get('permissionGroupCodes')
        return self


class PerfTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        is_deleted: str = None,
        status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.id = id
        self.is_deleted = is_deleted
        self.status = status
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.status is not None:
            result['status'] = self.status
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AgoalCreateProgressHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalCreateProgressRequest(TeaModel):
    def __init__(
        self,
        kr_id: str = None,
        merge_into_latest_progress: bool = None,
        objective_id: str = None,
        plain_text: str = None,
        progress: int = None,
        progress_merge_period: str = None,
    ):
        self.kr_id = kr_id
        self.merge_into_latest_progress = merge_into_latest_progress
        self.objective_id = objective_id
        self.plain_text = plain_text
        self.progress = progress
        self.progress_merge_period = progress_merge_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.merge_into_latest_progress is not None:
            result['mergeIntoLatestProgress'] = self.merge_into_latest_progress
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.plain_text is not None:
            result['plainText'] = self.plain_text
        if self.progress is not None:
            result['progress'] = self.progress
        if self.progress_merge_period is not None:
            result['progressMergePeriod'] = self.progress_merge_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('mergeIntoLatestProgress') is not None:
            self.merge_into_latest_progress = m.get('mergeIntoLatestProgress')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('plainText') is not None:
            self.plain_text = m.get('plainText')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('progressMergePeriod') is not None:
            self.progress_merge_period = m.get('progressMergePeriod')
        return self


class AgoalCreateProgressResponseBody(TeaModel):
    def __init__(
        self,
        content: OpenAgoalProgressDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = OpenAgoalProgressDTO()
            self.content = temp_model.from_map(m['content'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalCreateProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalCreateProgressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalCreateProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalEntityCreateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalEntityCreateRequest(TeaModel):
    def __init__(
        self,
        body: List[Entity] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Entity()
                self.body.append(temp_model.from_map(k))
        return self


class AgoalEntityCreateResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalEntityCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalEntityCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalEntityCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalEntityUpdateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalEntityUpdateRequest(TeaModel):
    def __init__(
        self,
        body: List[Entity] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Entity()
                self.body.append(temp_model.from_map(k))
        return self


class AgoalEntityUpdateResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalEntityUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalEntityUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalEntityUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalFieldUpdateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalFieldUpdateRequestBody(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        field_code: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_type = entity_type
        # This parameter is required.
        self.field_code = field_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['entityId'] = self.entity_id
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.field_code is not None:
            result['fieldCode'] = self.field_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AgoalFieldUpdateRequest(TeaModel):
    def __init__(
        self,
        body: AgoalFieldUpdateRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AgoalFieldUpdateRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalFieldUpdateShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class AgoalFieldUpdateResponseBody(TeaModel):
    def __init__(
        self,
        content: bool = None,
        request_id: str = None,
        success: str = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalFieldUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalFieldUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalFieldUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalObjectiveKeyActionListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalObjectiveKeyActionListRequest(TeaModel):
    def __init__(
        self,
        ding_user_id: str = None,
        key_result_id: str = None,
        objective_id: str = None,
    ):
        # This parameter is required.
        self.ding_user_id = ding_user_id
        self.key_result_id = key_result_id
        # This parameter is required.
        self.objective_id = objective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_user_id is not None:
            result['dingUserId'] = self.ding_user_id
        if self.key_result_id is not None:
            result['keyResultId'] = self.key_result_id
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingUserId') is not None:
            self.ding_user_id = m.get('dingUserId')
        if m.get('keyResultId') is not None:
            self.key_result_id = m.get('keyResultId')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        return self


class AgoalObjectiveKeyActionListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenAgoalKeyActionDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenAgoalKeyActionDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalObjectiveKeyActionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalObjectiveKeyActionListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalObjectiveKeyActionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalObjectiveRulePeriodListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalObjectiveRulePeriodListRequest(TeaModel):
    def __init__(
        self,
        objective_rule_id: str = None,
    ):
        # This parameter is required.
        self.objective_rule_id = objective_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_rule_id is not None:
            result['objectiveRuleId'] = self.objective_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveRuleId') is not None:
            self.objective_rule_id = m.get('objectiveRuleId')
        return self


class AgoalObjectiveRulePeriodListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenObjectiveRulePeriodDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenObjectiveRulePeriodDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalObjectiveRulePeriodListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalObjectiveRulePeriodListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalObjectiveRulePeriodListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalOrgObjectiveListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalOrgObjectiveListRequest(TeaModel):
    def __init__(
        self,
        ding_team_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period_id: str = None,
    ):
        self.ding_team_id = ding_team_id
        # This parameter is required.
        self.page_number = page_number
        self.page_size = page_size
        self.period_id = period_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_team_id is not None:
            result['dingTeamId'] = self.ding_team_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.period_id is not None:
            result['periodId'] = self.period_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingTeamId') is not None:
            self.ding_team_id = m.get('dingTeamId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        return self


class AgoalOrgObjectiveListResponseBody(TeaModel):
    def __init__(
        self,
        content: OpenAgoalOrgObjectiveListDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = OpenAgoalOrgObjectiveListDTO()
            self.content = temp_model.from_map(m['content'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalOrgObjectiveListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalOrgObjectiveListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalOrgObjectiveListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalOrgObjectiveQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalOrgObjectiveQueryRequest(TeaModel):
    def __init__(
        self,
        objective_id: str = None,
    ):
        # This parameter is required.
        self.objective_id = objective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        return self


class AgoalOrgObjectiveQueryResponseBody(TeaModel):
    def __init__(
        self,
        content: OpenAgoalOrgObjectiveDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = OpenAgoalOrgObjectiveDTO()
            self.content = temp_model.from_map(m['content'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalOrgObjectiveQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalOrgObjectiveQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalOrgObjectiveQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalOrgObjectiveRuleListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalOrgObjectiveRuleListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenOrgObjectiveRuleDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenOrgObjectiveRuleDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalOrgObjectiveRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalOrgObjectiveRuleListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalOrgObjectiveRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalPerfTaskCreateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalPerfTaskCreateRequest(TeaModel):
    def __init__(
        self,
        body: List[PerfTask] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = PerfTask()
                self.body.append(temp_model.from_map(k))
        return self


class AgoalPerfTaskCreateResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalPerfTaskCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalPerfTaskCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalPerfTaskCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalPerfTaskUpdateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalPerfTaskUpdateRequest(TeaModel):
    def __init__(
        self,
        body: List[PerfTask] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = PerfTask()
                self.body.append(temp_model.from_map(k))
        return self


class AgoalPerfTaskUpdateResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalPerfTaskUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalPerfTaskUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalPerfTaskUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalPeriodListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalPeriodListRequestBody(TeaModel):
    def __init__(
        self,
        period_types: List[str] = None,
    ):
        self.period_types = period_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_types is not None:
            result['periodTypes'] = self.period_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('periodTypes') is not None:
            self.period_types = m.get('periodTypes')
        return self


class AgoalPeriodListRequest(TeaModel):
    def __init__(
        self,
        body: AgoalPeriodListRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AgoalPeriodListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalPeriodListShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class AgoalPeriodListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenAgoalPeriodDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenAgoalPeriodDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalPeriodListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalPeriodListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalPeriodListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalSendMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalSendMessageRequest(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        params: str = None,
        pc_url: str = None,
        source_ding_user_id: str = None,
        target_ding_user_ids: List[str] = None,
        template_id: str = None,
    ):
        # This parameter is required.
        self.mobile_url = mobile_url
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.pc_url = pc_url
        # This parameter is required.
        self.source_ding_user_id = source_ding_user_id
        # This parameter is required.
        self.target_ding_user_ids = target_ding_user_ids
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.params is not None:
            result['params'] = self.params
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.source_ding_user_id is not None:
            result['sourceDingUserId'] = self.source_ding_user_id
        if self.target_ding_user_ids is not None:
            result['targetDingUserIds'] = self.target_ding_user_ids
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('sourceDingUserId') is not None:
            self.source_ding_user_id = m.get('sourceDingUserId')
        if m.get('targetDingUserIds') is not None:
            self.target_ding_user_ids = m.get('targetDingUserIds')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class AgoalSendMessageResponseBody(TeaModel):
    def __init__(
        self,
        content: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalSendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalSendMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalSendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalUserAdminListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalUserAdminListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenUserAdminDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.content = content
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenUserAdminDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalUserAdminListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalUserAdminListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalUserAdminListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalUserObjectiveListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalUserObjectiveListRequest(TeaModel):
    def __init__(
        self,
        ding_user_id: str = None,
        objective_rule_id: str = None,
        period_ids: List[str] = None,
    ):
        # This parameter is required.
        self.ding_user_id = ding_user_id
        # This parameter is required.
        self.objective_rule_id = objective_rule_id
        # This parameter is required.
        self.period_ids = period_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_user_id is not None:
            result['dingUserId'] = self.ding_user_id
        if self.objective_rule_id is not None:
            result['objectiveRuleId'] = self.objective_rule_id
        if self.period_ids is not None:
            result['periodIds'] = self.period_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingUserId') is not None:
            self.ding_user_id = m.get('dingUserId')
        if m.get('objectiveRuleId') is not None:
            self.objective_rule_id = m.get('objectiveRuleId')
        if m.get('periodIds') is not None:
            self.period_ids = m.get('periodIds')
        return self


class AgoalUserObjectiveListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenAgoalObjectiveDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenAgoalObjectiveDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalUserObjectiveListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalUserObjectiveListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalUserObjectiveListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgoalUserSubAdminListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class AgoalUserSubAdminListRequest(TeaModel):
    def __init__(
        self,
        func_permission_group: str = None,
    ):
        self.func_permission_group = func_permission_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.func_permission_group is not None:
            result['funcPermissionGroup'] = self.func_permission_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('funcPermissionGroup') is not None:
            self.func_permission_group = m.get('funcPermissionGroup')
        return self


class AgoalUserSubAdminListResponseBody(TeaModel):
    def __init__(
        self,
        content: List[OpenUserSubAdminDTO] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['content'] = []
        if self.content is not None:
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k in m.get('content'):
                temp_model = OpenUserSubAdminDTO()
                self.content.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AgoalUserSubAdminListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgoalUserSubAdminListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AgoalUserSubAdminListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


