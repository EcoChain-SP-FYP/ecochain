pragma solidity >= 0.5.0;

contract HelloWorld3 {

    string public payload;
	string public moisture;
	uint mlvl;
	string temp;
    string humid;
	string light;
	
    function setPayload(string memory content, uint content2, string memory content3, string memory content4, string memory content5) public {
        moisture = content;
		mlvl = content2;
		temp = content3;
		humid = content4;
		light = content5;
    }

    function sayHello() public pure returns (string memory) {
        return 'Hello World 3!';
    }
}