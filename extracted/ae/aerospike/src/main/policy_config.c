/*******************************************************************************
 * Copyright 2017-2021 Aerospike, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/
#include <stdint.h>

#include "policy_config.h"

as_status set_optional_key(as_policy_key *target_ptr, PyObject *py_policy,
                           const char *name);
as_status set_optional_replica(as_policy_replica *target_ptr,
                               PyObject *py_policy, const char *name);
as_status set_optional_commit_level(as_policy_commit_level *target_ptr,
                                    PyObject *py_policy, const char *name);
as_status set_optional_ap_read_mode(as_policy_read_mode_ap *target_ptr,
                                    PyObject *py_policy, const char *name);
as_status set_optional_sc_read_mode(as_policy_read_mode_sc *target_ptr,
                                    PyObject *py_policy, const char *name);
as_status set_optional_gen(as_policy_gen *target_ptr, PyObject *py_policy,
                           const char *name);
as_status set_optional_exists(as_policy_exists *target_ptr, PyObject *py_policy,
                              const char *name);
as_status get_uint32_value(PyObject *py_policy_val, uint32_t *return_uint32);
as_status set_optional_int_property(int *property_ptr, PyObject *py_policy,
                                    const char *field_name);

/*
 * py_policies must exist, and be a dictionary
 */
as_status set_subpolicies(as_config *config, PyObject *py_policies)
{

    as_status set_policy_status = AEROSPIKE_OK;

    PyObject *read_policy = PyDict_GetItemString(py_policies, "read");
    set_policy_status = set_read_policy(&config->policies.read, read_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *write_policy = PyDict_GetItemString(py_policies, "write");
    set_policy_status = set_write_policy(&config->policies.write, write_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *apply_policy = PyDict_GetItemString(py_policies, "apply");
    set_policy_status = set_apply_policy(&config->policies.apply, apply_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *remove_policy = PyDict_GetItemString(py_policies, "remove");
    set_policy_status =
        set_remove_policy(&config->policies.remove, remove_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *query_policy = PyDict_GetItemString(py_policies, "query");
    set_policy_status = set_query_policy(&config->policies.query, query_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *scan_policy = PyDict_GetItemString(py_policies, "scan");
    set_policy_status = set_scan_policy(&config->policies.scan, scan_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *operate_policy = PyDict_GetItemString(py_policies, "operate");
    set_policy_status =
        set_operate_policy(&config->policies.operate, operate_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *batch_policy = PyDict_GetItemString(py_policies, "batch");
    set_policy_status = set_batch_policy(&config->policies.batch, batch_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *info_policy = PyDict_GetItemString(py_policies, "info");
    set_policy_status = set_info_policy(&config->policies.info, info_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *admin_policy = PyDict_GetItemString(py_policies, "admin");
    set_policy_status = set_admin_policy(&config->policies.admin, admin_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *batch_apply_policy =
        PyDict_GetItemString(py_policies, "batch_apply");
    set_policy_status = set_batch_apply_policy(&config->policies.batch_apply,
                                               batch_apply_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *batch_remove_policy =
        PyDict_GetItemString(py_policies, "batch_remove");
    set_policy_status = set_batch_remove_policy(&config->policies.batch_remove,
                                                batch_remove_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *batch_write_policy =
        PyDict_GetItemString(py_policies, "batch_write");
    set_policy_status = set_batch_write_policy(&config->policies.batch_write,
                                               batch_write_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    PyObject *batch_parent_write_policy =
        PyDict_GetItemString(py_policies, "batch_parent_write");
    set_policy_status = set_batch_policy(&config->policies.batch_parent_write,
                                         batch_parent_write_policy);
    if (set_policy_status != AEROSPIKE_OK) {
        return set_policy_status;
    }

    const char *batch_policy_names[] = {"txn_verify", "txn_roll"};
    as_policy_batch *batch_policies[] = {&config->policies.txn_verify,
                                         &config->policies.txn_roll};
    for (unsigned long i = 0;
         i < sizeof(batch_policy_names) / sizeof(batch_policy_names[0]); i++) {
        PyObject *py_batch_policy =
            PyDict_GetItemString(py_policies, batch_policy_names[i]);
        set_policy_status =
            set_batch_policy(batch_policies[i], py_batch_policy);
        if (set_policy_status != AEROSPIKE_OK) {
            return set_policy_status;
        }
    }

    return AEROSPIKE_OK;
}

as_status set_read_policy(as_policy_read *read_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&read_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&read_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_replica(&read_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&read_policy->deserialize, py_policy,
                                        "deserialize");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_ap_read_mode(&read_policy->read_mode_ap, py_policy,
                                       "read_mode_ap");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_sc_read_mode(&read_policy->read_mode_sc, py_policy,
                                       "read_mode_sc");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_int_property(&read_policy->read_touch_ttl_percent,
                                       py_policy, "read_touch_ttl_percent");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_write_policy(as_policy_write *write_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&write_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&write_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_replica(&write_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_commit_level(&write_policy->commit_level, py_policy,
                                       "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_gen(&write_policy->gen, py_policy, "gen");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_exists(&write_policy->exists, py_policy, "exists");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(&write_policy->ttl, py_policy, "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(
        (uint32_t *)&write_policy->compression_threshold, py_policy,
        "compression_threshold");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&write_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_apply_policy(as_policy_apply *apply_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&apply_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&apply_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_replica(&apply_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(&apply_policy->ttl, py_policy, "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_commit_level(&apply_policy->commit_level, py_policy,
                                       "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&apply_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_remove_policy(as_policy_remove *remove_policy,
                            PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&remove_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&remove_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status =
        set_optional_replica(&remove_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_commit_level(&remove_policy->commit_level, py_policy,
                                       "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_gen(&remove_policy->gen, py_policy, "gen");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&remove_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_query_policy(as_policy_query *query_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&query_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&query_policy->deserialize, py_policy,
                                        "deserialize");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_replica(&query_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    PyObject *py_expected_duration =
        PyDict_GetItemString(py_policy, "expected_duration");
    if (py_expected_duration) {
        if (!PyLong_CheckExact(py_expected_duration)) {
            return AEROSPIKE_ERR_PARAM;
        }
        query_policy->expected_duration =
            (as_query_duration)PyLong_AsLong(py_expected_duration);
    }

    return AEROSPIKE_OK;
}

as_status set_scan_policy(as_policy_scan *scan_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }
    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&scan_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&scan_policy->durable_delete, py_policy,
                                        "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(&scan_policy->ttl, py_policy, "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_replica(&scan_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_operate_policy(as_policy_operate *operate_policy,
                             PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&operate_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&operate_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status =
        set_optional_replica(&operate_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_commit_level(&operate_policy->commit_level, py_policy,
                                       "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status =
        set_optional_uint32_property(&operate_policy->ttl, py_policy, "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_gen(&operate_policy->gen, py_policy, "gen");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&operate_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&operate_policy->deserialize, py_policy,
                                        "deserialize");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    // 4.0.0 onwards

    status = set_optional_ap_read_mode(&operate_policy->read_mode_ap, py_policy,
                                       "read_mode_ap");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_sc_read_mode(&operate_policy->read_mode_sc, py_policy,
                                       "read_mode_sc");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_int_property(&operate_policy->read_touch_ttl_percent,
                                       py_policy, "read_touch_ttl_percent");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_batch_policy(as_policy_batch *batch_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_base_policy(&batch_policy->base, py_policy);
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_policy->concurrent, py_policy,
                                        "concurrent");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_policy->allow_inline, py_policy,
                                        "allow_inline");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_policy->deserialize, py_policy,
                                        "deserialize");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_ap_read_mode(&batch_policy->read_mode_ap, py_policy,
                                       "read_mode_ap");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_sc_read_mode(&batch_policy->read_mode_sc, py_policy,
                                       "read_mode_sc");
    if (status != AEROSPIKE_OK) {
        return status;
    }
    status = set_optional_replica(&batch_policy->replica, py_policy, "replica");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_int_property(&batch_policy->read_touch_ttl_percent,
                                       py_policy, "read_touch_ttl_percent");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_info_policy(as_policy_info *info_policy, PyObject *py_policy)
{
    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_uint32_property((uint32_t *)&info_policy->timeout,
                                          py_policy, "timeout");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_admin_policy(as_policy_admin *admin_policy, PyObject *py_policy)
{
    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_uint32_property(&admin_policy->timeout, py_policy,
                                          "timeout");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

// For batch write, batch apply, and batch remove policies:
// Don't set expressions field since it depends on the client's
// serialization policy

as_status set_batch_apply_policy(as_policy_batch_apply *batch_apply_policy,
                                 PyObject *py_policy)
{
    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_commit_level(&batch_apply_policy->commit_level,
                                       py_policy, "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_apply_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&batch_apply_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(&batch_apply_policy->ttl, py_policy,
                                          "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_batch_write_policy(as_policy_batch_write *batch_write_policy,
                                 PyObject *py_policy)
{
    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_commit_level(&batch_write_policy->commit_level,
                                       py_policy, "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_write_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status =
        set_optional_exists(&batch_write_policy->exists, py_policy, "exists");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(&batch_write_policy->ttl, py_policy,
                                          "ttl");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_gen(&batch_write_policy->gen, py_policy, "gen");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&batch_write_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_batch_remove_policy(as_policy_batch_remove *batch_remove_policy,
                                  PyObject *py_policy)
{
    as_status status = AEROSPIKE_OK;
    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_commit_level(&batch_remove_policy->commit_level,
                                       py_policy, "commit_level");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_bool_property(&batch_remove_policy->durable_delete,
                                        py_policy, "durable_delete");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_gen(&batch_remove_policy->gen, py_policy, "gen");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint16_property(&batch_remove_policy->generation,
                                          py_policy, "generation");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_key(&batch_remove_policy->key, py_policy, "key");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status set_base_policy(as_policy_base *base_policy, PyObject *py_policy)
{

    as_status status = AEROSPIKE_OK;

    if (!py_policy) {
        return AEROSPIKE_OK;
    }

    if (!PyDict_Check(py_policy)) {
        return AEROSPIKE_ERR_PARAM;
    }

    status = set_optional_uint32_property(
        (uint32_t *)&base_policy->total_timeout, py_policy, "total_timeout");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(
        (uint32_t *)&base_policy->socket_timeout, py_policy, "socket_timeout");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property((uint32_t *)&base_policy->max_retries,
                                          py_policy, "max_retries");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    status = set_optional_uint32_property(
        (uint32_t *)&base_policy->sleep_between_retries, py_policy,
        "sleep_between_retries");
    if (status != AEROSPIKE_OK) {
        return status;
    }

    return AEROSPIKE_OK;
}

as_status get_uint32_value(PyObject *py_policy_val, uint32_t *return_uint32)
{
    long long int uint32_max = 0xFFFFFFFF;

    if (!py_policy_val) {
        return AEROSPIKE_ERR_PARAM;
    }
    if (PyLong_Check(py_policy_val)) {
        long int_value = PyLong_AsLong(py_policy_val);

        if (int_value == -1 && PyErr_Occurred()) {
            PyErr_Clear();
            return AEROSPIKE_ERR_PARAM;
        }

        if (int_value < 0 || int_value > uint32_max) {
            return AEROSPIKE_ERR_PARAM;
        }

        *return_uint32 = (uint32_t)int_value;
        return AEROSPIKE_OK;
    }
    return AEROSPIKE_ERR_PARAM;
}

as_status set_optional_uint32_property(uint32_t *target_ptr,
                                       PyObject *py_policy, const char *name)
{
    PyObject *py_policy_val = NULL;
    long long int uint32_max = 0xFFFFFFFF;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val) {
        return AEROSPIKE_OK;
    }
    if (PyLong_Check(py_policy_val)) {
        long int_value = PyLong_AsLong(py_policy_val);

        if (int_value == -1 && PyErr_Occurred()) {
            // This wasn't a valid int, or was too large
            // We are handling the error ourselves, so clear the overflow error
            PyErr_Clear();
            return AEROSPIKE_ERR_PARAM;

            /* If the number was less than zero, or would not fit in a uint32, error */
        }
        if (int_value < 0 || int_value > uint32_max) {
            return AEROSPIKE_ERR_PARAM;
        }

        *target_ptr = (uint32_t)int_value;
        return AEROSPIKE_OK;
    }
    return AEROSPIKE_ERR_PARAM;
}

as_status set_optional_uint16_property(uint16_t *target_ptr,
                                       PyObject *py_policy, const char *name)
{
    // Assume py_policy is a Python dictionary
    PyObject *py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val) {
        // Key doesn't exist in policy
        return AEROSPIKE_OK;
    }
    Py_INCREF(py_policy_val);

    if (!PyLong_Check(py_policy_val)) {
        return AEROSPIKE_ERR_PARAM;
    }

    long int_value = PyLong_AsLong(py_policy_val);
    if (int_value == -1 && PyErr_Occurred()) {
        // This wasn't a valid int, or was too large
        // We are handling the error ourselves, so clear the overflow error
        PyErr_Clear();
        return AEROSPIKE_ERR_PARAM;

        /* If the number was less than zero, or would not fit in a uint16, error */
    }
    if (int_value < 0 || int_value > UINT16_MAX) {
        return AEROSPIKE_ERR_PARAM;
    }

    *target_ptr = (uint16_t)int_value;
    return AEROSPIKE_OK;
}

as_status set_optional_bool_property(bool *target_ptr, PyObject *py_policy,
                                     const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val) {
        return AEROSPIKE_OK;
    }
    if (PyBool_Check(py_policy_val)) {
        *target_ptr = PyObject_IsTrue(py_policy_val);
        return AEROSPIKE_OK;
    }
    return AEROSPIKE_ERR_PARAM;
}

as_status set_optional_key(as_policy_key *target_ptr, PyObject *py_policy,
                           const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_key)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_replica(as_policy_replica *target_ptr,
                               PyObject *py_policy, const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_replica)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_commit_level(as_policy_commit_level *target_ptr,
                                    PyObject *py_policy, const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_commit_level)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_ap_read_mode(as_policy_read_mode_ap *target_ptr,
                                    PyObject *py_policy, const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_read_mode_ap)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_sc_read_mode(as_policy_read_mode_sc *target_ptr,
                                    PyObject *py_policy, const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_read_mode_sc)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_gen(as_policy_gen *target_ptr, PyObject *py_policy,
                           const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_gen)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_exists(as_policy_exists *target_ptr, PyObject *py_policy,
                              const char *name)
{
    PyObject *py_policy_val = NULL;
    if (!py_policy || !PyDict_Check(py_policy)) {
        return AEROSPIKE_OK;
    }

    py_policy_val = PyDict_GetItemString(py_policy, name);
    if (!py_policy_val || py_policy_val == Py_None) {
        return AEROSPIKE_OK;
    }

    uint32_t out_uint32;
    as_status status = get_uint32_value(py_policy_val, &out_uint32);
    if (status != AEROSPIKE_OK) {
        return status;
    }
    *target_ptr = (as_policy_exists)out_uint32;
    return AEROSPIKE_OK;
}

as_status set_optional_int_property(int *property_ptr, PyObject *py_policy,
                                    const char *field_name)
{
    PyObject *py_field = PyDict_GetItemString(py_policy, field_name);
    if (py_field) {
        if (PyLong_Check(py_field)) {
            *property_ptr = (int)PyLong_AsLong(py_field);
        }
        else {
            return AEROSPIKE_ERR_PARAM;
        }
    }

    return AEROSPIKE_OK;
}
