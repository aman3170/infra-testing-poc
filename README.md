# infra-testing-poc
Step-by-step guide to showcases Testinfra, InSpec, and Molecule for infrastructure testing

1. Testinfra

pytest --connection=docker --hosts=${container_id} test_nginx.py
============================================================================================= test session starts ==============================================================================================
platform darwin -- Python 3.13.3, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/amanpatel/Documents/POC_projects/infra-testing-poc/testinfra
plugins: testinfra-10.2.2, testinfra-6.0.0
collected 1 item                                                                                                                                                                                               

test_nginx.py .                                                                                                                                                                                          [100%]

============================================================================================== 1 passed in 0.27s ===============================================================================================

2. InSpec

inspec exec . -t docker://inspec-nginx

Profile:   InSpec Profile (.)
Version:   0.1.0
Target:    docker://<container_id>
Target ID: <target_id>

  ✔  tmp-1.0: Create /tmp directory
     ✔  File /tmp is expected to be directory

  File /tmp
     ✔  is expected to be directory

Profile Summary: 1 successful control, 0 control failures, 0 controls skipped
Test Summary: 2 successful, 0 failures, 0 skipped

3. Molecule

