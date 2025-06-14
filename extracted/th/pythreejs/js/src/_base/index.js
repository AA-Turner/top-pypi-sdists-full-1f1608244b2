//
// This file auto-generated with generate-wrappers.js
//
// Load all three.js python wrappers
var loadedModules = [
    require('./Preview.js'),
    require('./Renderable.js'),
    require('./RendererPool.js'),
    require('./Three.js'),
    require('./enums.js'),
    require('./serializers.js'),
    require('./utils.js'),
];

for (var i in loadedModules) {
    if (Object.prototype.hasOwnProperty.call(loadedModules, i)) {
        var loadedModule = loadedModules[i];
        for (var target_name in loadedModule) {
            if (Object.prototype.hasOwnProperty.call(loadedModule, target_name)) {
                module.exports[target_name] = loadedModule[target_name];
            }
        }
    }
}

