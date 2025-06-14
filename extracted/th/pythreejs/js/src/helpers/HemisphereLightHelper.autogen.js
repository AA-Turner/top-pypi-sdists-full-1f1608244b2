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

var HemisphereLightModel = require('../lights/HemisphereLight.autogen.js').HemisphereLightModel;

class HemisphereLightHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            light: null,
            size: 1,
            color: "#ffffff",
            type: "HemisphereLightHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.HemisphereLightHelper(
            this.convertThreeTypeModelToThree(this.get('light'), 'light'),
            this.convertFloatModelToThree(this.get('size'), 'size'),
            this.convertColorModelToThree(this.get('color'), 'color')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('light');

        this.props_created_by_three['matrixAutoUpdate'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['light'] = 'convertThreeType';
        this.property_converters['size'] = 'convertFloat';
        this.property_converters['color'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

HemisphereLightHelperModel.model_name = 'HemisphereLightHelperModel';
HemisphereLightHelperModel.serializers = {
    ...Object3DModel.serializers,
    light: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    HemisphereLightHelperModel: HemisphereLightHelperModel,
};
