//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class WebGLRenderTargetCubeModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.WebGLRenderTargetCube();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

WebGLRenderTargetCubeModel.model_name = 'WebGLRenderTargetCubeModel';
WebGLRenderTargetCubeModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    WebGLRenderTargetCubeModel: WebGLRenderTargetCubeModel,
};
