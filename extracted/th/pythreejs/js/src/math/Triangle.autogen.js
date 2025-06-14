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


class TriangleModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            a: [0,0,0],
            b: [0,0,0],
            c: [0,0,0],

        });
    }

    constructThreeObject() {

        var result = new THREE.Triangle(
            this.convertVectorModelToThree(this.get('a'), 'a'),
            this.convertVectorModelToThree(this.get('b'), 'b'),
            this.convertVectorModelToThree(this.get('c'), 'c')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['a'] = 'convertVector';
        this.property_converters['b'] = 'convertVector';
        this.property_converters['c'] = 'convertVector';

        this.property_assigners['a'] = 'assignVector';
        this.property_assigners['b'] = 'assignVector';
        this.property_assigners['c'] = 'assignVector';

    }
}

TriangleModel.model_name = 'TriangleModel';
TriangleModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    TriangleModel: TriangleModel,
};
