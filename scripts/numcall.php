<?php
function getmsg() {
system('stty -echo');
$msg = trim(fgets(STDIN));
system('stty echo');
return $msg;
}
function h($x) {
echo "calling '$x'...\n";
usleep(500000);
echo "...\n";
usleep(750000);
echo "...\n";
usleep(250000);
for ($i = 1; $i <= 5; $i++) {
echo "brrrrr\n";
usleep(850000);
}
usleep(100000);
echo "...\n";
usleep(750000);
echo "please leave a message at the beep\n";
sleep(2);
echo "beeep\n";
usleep(500000);
echo "enter message:\n";
$msg = getmsg();
for ($i = 0; $i < strlen($msg); $i++) {
usleep(250000);
echo $msg[$i];
}
echo "\n";
usleep(500000);
echo "*you hang up*\n";
}
function init() {
echo "enter number to call:\n";
return readline();
}
function main() {
return h(init());
}
main();
?>