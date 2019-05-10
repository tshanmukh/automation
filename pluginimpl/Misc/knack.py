import pandas as pd

from openpyxl import load_workbook

# writer = pd.ExcelWriter('/home/rupesh/Downloads/sheet_syed.xlsx', engine='openpyxl')
# wb  = writer.book
# df = pd.DataFrame({'Plugin Version': 'BE',
#                   'SL': 'BE'})
# df.to_excel(writer, index=False)
# wb.save('/home/rupesh/Downloads/sheet_syed.xlsx')
# Plugin Version   SL
abc = "brocade-san-switch calix-e7 cisco-5500-wireless cisco-9300 cisco-pixfirewall cisco-sf300 dell-rac eaton-powerware evertz-7000 fujitsu-flashwave-7420 gigamon-gigavue hpux motorola-apex motorola-bsr-64000 motorola-sem netapp-ocum solaris-server toshiba-ups 1finity-t30-10gig-muxponder adtran-opti-6100-mx alcatel-7705 alpha-ups cisco-ace-4710 cisco-asa-5520 cisco-mgx eltek motorola-dsr-6000 apc-smart-ups argus-cxc-controller cisco-9500 cisco-asa-5500 cisco-d9000 cisco-ibm-module cisco-ons15454-snmp jdsu-rsam juniper-j4350 juniper-ssg metrobility-radiance-5k motorola-sep schneider-ion sencore-mrd vmware-vcenter-server accedian-nid alcatel-1830-pss arbornet-peakflow arris-bnc arris-egt-encoder asco-5210 axino ciena-5150 cisco-3000 cisco-3650 cisco-7200 cisco-asr920 cisco7206VXR-router docs3.0-arris-c4 fujitsu-flashwave-4100 fujitsu-flashwave-4100es-r10 fujitsu-flashwave-cds infoblox-grid juniper-ssg-100 packeteer-packetshaper scte-hms-ups symmetricom-timecreator-1000 valere-dc-power acmepacket-net-net-4000 cisco-2600 cisco-3550 cisco-4900m cisco-881 cisco-csr1000v cisco-d9850 cisco-dcm-9900 cisco-me-6500 cisco-nexus-3500 cisco-nexus-7000 cordex-cx dell-isilon dragonwave-horizon-compact edgewater-edgemarc empirix f5-big-ip harmonic-electra-8200 ibm-system-x3550 metaswitch-sbc microsoft-windows motorola-nc-1500 motorola-om2000 motorola-radd-6000 netomnia-server nuera-orca-btx-4k rgb-sep tasman-6300 verivue nagios-pm a10thunder-3430 aastra-videorunner adtran-3140 adtran-ta-4303 adva-fsp-150cc arris-cherry-picker-cap1000 barracuda-antispam-server benu-meg broadsoft-broadworks calix-c7 calix-e5-111 calix-e7-20 ceragon-ip-20 ciena-3900 cisco-2610 cisco-asr903 cisco-d9800 cisco-ncs-55a cisco-ncs5501 comptel-nt-system dantel-webmon eaton-powerxpertcard-ups ellacoya-e100 ericsson-edn312xp ericsson-esn108 ericsson-esn410 fujitsu-flashwave-4010 fujitsu-flashwave-4500-r11 fujitsu-flashwave-9500-r9 ironport-antispam-server juniper-netscreen-isg2000 metaswitch-ems motorola-bnc powerware scte-myers syes-broadcast-transmitter syes-pcm-150-uhf tekelec-eagle zhone-malc acmepacket-net-net-6000 adtran-ta-5000-snmp-comporium cisco-12416 cisco-12810 cisco-2800 cisco-3900 cisco-7300 cisco-800 cisco-ie-4000 cisco-meraki cisco-prime-infrastructure cisco-vg224 dragonwave-hemc fujitsu-flashwave-7500 ge-ml genband-g9 harmonic-cp9000 harmonic-prostream1000 ineoquest-cricket juniper-acx5048 juniper-netscreen-5gt moseley-nex-gen-x motorola-arpd motorola-mmc mrv-os9xx nortel-cs2000 palo-alto-5050 procera-packetlogic rad-etx rad-ipmux rad-rici telcobridges-tmg3200 arris-e6000 hp-proliant cisco-nexus-5000 alcatel-7360 f5 alcatel-7210 alcatel-7750 a10thunder3030s actelis-ml2300 adtran-600 adtran-mx-2800 adtran-mx408e adtran-opti-6100 adtran-ta-1500 adtran-ta-5000-snmp adva-fsp-3000-snmp adva-fsp-r7-snmp airframe-server akcp-sensorprobe8-x60 alcatel-7700 alcatel-omc-ran alcatel-oms1350 arris-apex1000 arris-c4 aurora-ge4132m-gpon aurora-system3000 benning bnt-gbesm calix-c7-snmp calix-e3-12c calix-e5-110 canoga-perkins carrier-access-mux casa-c10g ciena-3916 ciena-3930 ciena-5140 ciena-5142 ciena-6500 ciena-cpl-dwdm cisco-12404 cisco-1600 cisco-1720 cisco-1800 cisco-1841 cisco-2431 cisco-2432 cisco-2611 cisco-2620 cisco-2621 cisco-2651 cisco-2950 cisco-2960 cisco-3508 cisco-3512 cisco-3560 cisco-3600 cisco-3725 cisco-3745 cisco-3800-switch cisco-3845 cisco-3850 cisco-3925 cisco-4507 cisco-4924 cisco-4948 cisco-4948e cisco-6509 cisco-7140 cisco-7301 cisco-7304 cisco-7603 cisco-7606 cisco-7606s cisco-7609 cisco-8500 cisco-asa-5550 cisco-asa-5585x cisco-bts10200 cisco-continuum-dqa cisco-generic cisco-isr4000 cisco-me-1200 cisco-nexus-5596up cisco-prime-access-registrar comverse eltekhe-fp emc emerson-netsure-802 ericsson-ecn330 ericsson-edn312p ericsson-esn212 ericsson-ggsn ericsson-se600 ericsson-sgsn genband-c20 generic-docsis-modem harmonic-prostream huawei-m2000 huawei-u2000-snmp huawei-u2000 ibm-db2 ibm-mm infoblox-ib1050a infogin ipoque-dpi netguardian-216f nortel-ethernet-routing-switch-8600 nortel-ome-6110 ntest-fiberwatch omnitron-cwdm oracle-db peerapp sonus-sbc-5110 sun-sparc symmetricom-tp-5000 tellabs-accessmax valere-dc-power-bc2000 valere-dc-power-ver1.0 valere-dc-power-xc2100 veritas zhone-zms cisco-asr9000 alcatel-7450 cisco-nexus-9000 linux-server cisco-asr1000 cisco-3750 cisco-4900 cisco-me-3600 cisco-3800 cisco-isr-2911 ineoquest cisco-2900 emerson-netsure harmonic-proview-7110 mrv-lx-4000 actelis-ml600 cisco-12406 cisco-ons15310 cisco-ons15454 cisco-ons15600 fortinet-fortigate Juniper-srx-240 adc-higain-hmu-319 inca-4420 genband-sbc dps-netguardian-g4-g5 checkpoint-ngx ciena-5170 telco-3308 telco-8006 telco-systems-tmarc-300 telco-tmarc-3348s adtran-mx-2820-snmp adtran-mx4 bluecat-adonis brocade-icx6000 brocade-vdx6700 checkpoint-5k-6k-15k-23k ciena-6500-snmp dsctech-asn-controller endrun-tempus-lx ubiquiti-unifi-switch ubiquiti-unifi-wap ubiquiti foundary-brocade-mlx nortel-cpl nortel-cs-1500 nortel-ome-6500 dps-ng832a foundary-fastiron-edge-448 genband harmonic-encoder comptel-nt-system nortel-dms nortel-gsm-umts-atca-cs nortel-gsm-umts-atca-hlr nortel-gsm-umts-mg nortel-universal-sp nortel-wnms"
cdf = [plugin.lower() for plugin in abc.split(' ')]  # Reviewed list
print(len(cdf))

df = pd.read_csv('/home/sthummala/Downloads/sknack.csv')

count = 0
# print(df['ID'][2])

for i in df.index:
    # print(i)
    if df['ID'][i].lower() in cdf:
        print(df['ID'][i])
        df['Support Level'][i] = 'PS'
        # df['SL'][i] = 'BE'
        # print(df['Support Level'][i])
        count += 1
    else:
        df['Support Level'][i] = 'BE'
        # print(df['Support Level'][i])
df.to_excel("output.xlsx",index=False)
# for index, row in sh.iterrows():
#     print(row)
#     if row['Plugin'] in cdf:
#
#         # row['Plugin Version']=7
#         # row['SL']='PS'
#
#         # row['Plugin'].replace('6','7')
#         # row['SL'].replace('PS','BE')
#
#         # row['Plugin']=row['Plugin'].map({'Plugin': 7})
#
#         row['SL'].set_value('7')
#
#         row['Plugin'].set_value('BE')
#         count+=1
#
print(count)





