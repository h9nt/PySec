<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] != "GET") {
    http_response_code(405);
    exit;
}

function encrypt($n, $o) {
    $d = range(0, 255);
    $j = 0;
    for ($i = 0; $i < 256; $i++) {
        $j = ($j + $d[$i] + ord($o[$i % strlen($o)])) % 256;
        $temp = $d[$i];
        $d[$i] = $d[$j];
        $d[$j] = $temp;
    }

    $i = 0;
    $j = 0;
    $azar = '';

    for ($k = 0; $k < strlen($n); $k++) {
        $i = ($i + 1) % 256;
        $j = ($j + $d[$i]) % 256;
        $temp = $d[$i];
        $d[$i] = $d[$j];
        $d[$j] = $temp;
        $azar .= chr(ord($n[$k]) ^ $d[($d[$i] + $d[$j]) % 256]);
    }
    return base64_encode($azar);
}

function get_stub() {
    $path = "";
    $plaintext = file_get_contents($path);
    return encrypt($plaintext, 'MySecKey!**1');
}

echo json_encode([
    'stub' => get_stub(),
    'now' => time() * 1000
]);

?>
