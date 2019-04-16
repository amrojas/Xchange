<?php

require_once('sq_config.php');

// Set the permissions
$permissions = urlencode(
    "PAYMENTS_WRITE " .
    "PAYMENTS_READ"
 );

 // Display the OAuth link
echo '<a href="https://' .
_SQ_DOMAIN . _SQ_AUTHZ_URL .
'?client_id=' . _SQ_APP_ID .
'&scope=' . $permissions. '">Authorize this application</a>';

?>
