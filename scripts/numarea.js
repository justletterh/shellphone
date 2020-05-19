var readlineSync = require('readline-sync');
const codes = {"us":{"281":"houston, texas","404":"atlanta, georgia","713":"houston, texas","808":"hawaii","832":"houston, texas"}};
const us = codes["us"];
function thing(x) {
  var x=`${x}`;
  var c=0;
  var m='';
  if (x.charAt(0)=='1'){
    c=1;
    x=x.substring(1);
    m="\nit's from the united states";
  } else {
    m="\ni'm sorry but this script only supports the united states as of now";
  }
  console.log(`the number you gave me is '${x}'${m}`);
  var area = x.substring(0,3);
  if (area in us){
    console.log("and it's in "+us[area]);
  } else {
    console.log('that area code is not supported yet');
  }
}
function init() {
  var x = readlineSync.question('enter your number with the country code: ');
  const no=[" ","+","-","(",")"];
  no.forEach(function(value){
    x=x.split(value).join("");
  });
  return x;
}
function main() {
  thing(init());
}
main();