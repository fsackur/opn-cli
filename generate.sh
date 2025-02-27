opn-cli new api core diagnostics --api-output-dir /gitroot/upstream/opn-cli/opnsense_cli/api/core

opn-cli new command core diagnostics ping --tag settings --model-url https://raw.githubusercontent.com/opnsense/core/refs/heads/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Ping.xml --form-url https://raw.githubusercontent.com/opnsense/core/refs/heads/master/src/opnsense/mvc/app/controllers/OPNsense/Diagnostics/forms/ping.xml --command-output-dir /gitroot/upstream/opn-cli/opnsense_cli/commands/core/

docker build --tag opn-cli .
docker run -it -v .:/app/ --entrypoint pytest opn-cli "-k not acceptance"
