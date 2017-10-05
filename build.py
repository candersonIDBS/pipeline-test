from idbs_aws.templates.hosted_eworkbook.generate_stacks import eworkbook_generate

eworkbook_generate(
    customer_name='pipelinetest',
    region='eu-west-1',
    eworkbook_version='10221',
    domain='idbs-dev.com',
    vpc_cidr='10.100.0.0/16',
    keypair='canderson',
    idbs_ips=['194.168.169.49/32', '194.168.169.34/32', '194.168.169.33/32', '194.168.169.59/32',
              '194.168.169.32/32', '194.168.169.48/32'],
    customer_ips=['80.147.77.44/32', '141.6.11.0/24',
                  '141.6.11.51/32', '141.6.11.52/32', '103.249.80.178/32', '182.71.232.198/32',
                  '1.23.166.42/32', '62.225.157.82/32', '88.152.1.90/32', '87.139.72.59/32',
                  '80.4.63.186/32'],
    new_relic_ips=['52.28.221.96/32'],
    parameters={'BuiltBy': 'canderson', 'Owner': 'SRE', 'Purpose': 'Pipeline Test', 'Customer': 'BASF',
                'Product': '', 'PurchaseOrder': '', 'TerminationProtection': 'false',
                'MachineStateScheduling': 'dev-24/7', 'ArchitectureVersion': '1.3'},
    newrelic={'production': True},
    alert_logic={'install': False, 'tm_ami': 'ami-3430d75b', 'size': 'c4.large'},
    install_rds=True,
    rds_parameters={'family': 'oracle-se2-12.1',
                    'version': '12.1.0.2.v6',
                    'engine': 'oracle-se2',
                    'storage_type': 'gp2',
                    'instance_type': 'db.m4.large',
                    'multi_az': 'false',
                    'allocated_storage': '10',
                    # 'snapshot_id': 'msnapshot-hostedewbdb-basfmigration',
                    },
    rds_snapshots={'enable': False, 'backup_copy_region': False},
    development=False,
    enable_monitoring=True,
    # profile_name='devops',
    inventory=False,
    chemistry=False,
    hosted_puppet={'install': True, 'puppet_alerts': 'sre@idbs.com'},
    app_servers={'size': 'm4.xlarge', 'spot_price': False, 'min_count': 1, 'desired_count': 1, 'max_count': 3,
                 'os': 'CentOS'},
    ss_servers={'size': 'm4.xlarge', 'spot_price': False, 'min_count': 1, 'desired_count': 1, 'max_count': 3,
                'os': 'CentOS', 'bartender_labels': False},
    dry_run=False,
    alb=False,
    ssl_certs=True,
    health_tools=False,
    connectbot=False,
)
