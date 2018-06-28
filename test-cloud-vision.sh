API_KEY=AIzaSyBvbMcsev6snoYojFVBVwjSapCpGdyTheg
curl -v -s -H "Content-Type: application/json" \
    https://vision.googleapis.com/v1/images:annotate?key=${API_KEY} \
    --data-binary @request.json \
    -o response.json
