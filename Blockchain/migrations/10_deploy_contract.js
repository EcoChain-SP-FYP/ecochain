var HelloWorld = artifacts.require("HelloWorld3");

module.exports = function(deployer) {
    deployer.deploy(HelloWorld);
};