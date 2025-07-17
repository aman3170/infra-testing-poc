control 'nginx-package' do
  describe package('nginx') do
    it { should be_installed }
  end
end

control 'nginx-service' do
  describe service('nginx') do
    it { should be_running }
  end
end
