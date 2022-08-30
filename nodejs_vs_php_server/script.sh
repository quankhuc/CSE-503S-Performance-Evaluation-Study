ab -c 300 -n 2000 -r http://18.117.124.136/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/get.php
echo "----------------------------------------------------"
ab -c 300 -n 2000 -r -l http://18.117.124.136/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/post.php
echo "----------------------------------------------------"