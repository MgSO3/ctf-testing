<?php
$name = isset($_GET['name']) ? htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8') : 'Guest';
echo "<h1>Welcome back, " . $name . "!</h1>";
?>