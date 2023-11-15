```bash
curl --location http://localhost:8000/messages/question \
     -d '{"question": "hello, everyone"}' \
     -H 'Authorization: Bearer TOKEN' \
     --no-buffer
```