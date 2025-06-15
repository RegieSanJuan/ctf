<?php
require_once('flag.php');
$password_hash = "0e902564435691274142490923013038";
$salt = "f789bbc328a3d1a3";

if (isset($_GET['password'])) {
    $input = $_GET['password'];
    $hash = md5($salt . $input);
    if ($hash == $password_hash) {
        echo "=== FLAG START ===<br>";
        echo $flag . "<br>";
        echo "=== FLAG END ===<br>";
    }
}

echo highlight_file(__FILE__, true);
?>
