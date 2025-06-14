//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var Object3DModel = require('../core/Object3D.js').Object3DModel;

var Box3Model = require('../math/Box3.autogen.js').Box3Model;

class Box3HelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            box: null,
            color: "yellow",
            type: "Box3Helper",

        });
    }

    constructThreeObject() {

        var result = new THREE.Box3Helper(
            this.convertThreeTypeModelToThree(this.get('box'), 'box'),
            this.convertColorModelToThree(this.get('color'), 'color')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('box');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['box'] = 'convertThreeType';
        this.property_converters['color'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

Box3HelperModel.model_name = 'Box3HelperModel';
Box3HelperModel.serializers = {
    ...Object3DModel.serializers,
    box: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    Box3HelperModel: Box3HelperModel,
};
