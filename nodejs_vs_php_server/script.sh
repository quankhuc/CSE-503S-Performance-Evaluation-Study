ab -c 300 -n 2000 -r http://3.15.210.36/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/get.php
echo '------------------------------------------------------------------------------------------------------------------'
ab -p data.json -T application/json -c 300 -n 2000 -r -l http://3.15.210.36/CSE-503S-PERFORMANCE-EVALUATION-STUDY/nodejs_vs_php_server/post.php
echo '------------------------------------------------------------------------------------------------------------------'
ab -c 300 -n 2000 -r http://3.15.210.36:3000/
echo '------------------------------------------------------------------------------------------------------------------'
ab -p data.json -T application/json -c 300 -n 2000 -r -l http://3.15.210.36:3000/
echo '------------------------------------------------------------------------------------------------------------------'
