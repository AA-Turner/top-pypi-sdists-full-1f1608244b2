//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var LightShadowModel = require('./LightShadow.js').LightShadowModel;


class DirectionalLightShadowModel extends LightShadowModel {

    defaults() {
        return _.extend(LightShadowModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.DirectionalLightShadow();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightShadowModel.prototype.createPropertiesArrays.call(this);




    }
}

DirectionalLightShadowModel.model_name = 'DirectionalLightShadowModel';
DirectionalLightShadowModel.serializers = {
    ...LightShadowModel.serializers,
};

module.exports = {
    DirectionalLightShadowModel: DirectionalLightShadowModel,
};
