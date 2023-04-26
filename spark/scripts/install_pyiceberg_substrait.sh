BIN="/home/iceberg/bin"
VERSION="1.14.0"
curl -sSL "https://github.com/bufbuild/buf/releases/download/v${VERSION}/buf-$(uname -s)-$(uname -m)" -o "${BIN}/buf"
chmod +x "${BIN}/buf"
cd /home/iceberg/substrait
git clone --recursive https://github.com/vibhatha/pyiceberg_substrait.git
cd pyiceberg_substrait
git submodule sync --recursive
git submodule update --init --recursive
pip install protobuf==3.20.1 protoletariat==2.0.0 pytest==7.0.0 setuptools==61.0.0 setuptools_scm==6.2.0 ibis==3.2.0 ibis-substrait==2.28.1
cd substrait-python
git submodule sync --recursive
git submodule update --init --recursive
pip install -e .
cd ../
pip install -e .

