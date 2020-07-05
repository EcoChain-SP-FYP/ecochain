var Sensors = artifacts.require("Sensors");

module.exports = function(deployer) {
  deployer.deploy(Sensors);
};
