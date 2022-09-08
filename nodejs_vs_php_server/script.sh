echo 'Start testing GET endpoint of PHP server'
ab -c 300 -n 2000 -r http://3.15.210.36/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/get.php
echo '------------------------------------------------------------------------------------------------------------------'
echo 'Start testing POST endpoint of PHP server'
ab -p data.json -T application/json -c 300 -n 2000 -r -l http://3.15.210.36/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/post.php
echo '------------------------------------------------------------------------------------------------------------------'
echo 'Start testing GET endpoint of NodeJS server'
ab -c 300 -n 2000 -r http://3.15.210.36:3000/
echo '------------------------------------------------------------------------------------------------------------------'
echo 'Start testing POST endpoint of NodeJS server'
ab -p data.json -T application/json -c 300 -n 2000 -r -l http://3.15.210.36:3000/
echo '------------------------------------------------------------------------------------------------------------------'
