//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../../_base/serializers');

var ThreeModel = require('../../_base/Three.js').ThreeModel;


class EllipseCurveModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.EllipseCurve();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

EllipseCurveModel.model_name = 'EllipseCurveModel';
EllipseCurveModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    EllipseCurveModel: EllipseCurveModel,
};
