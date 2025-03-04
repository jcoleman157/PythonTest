"""
    Jacob Coleman, Ian Tasker
    Lab 04
    Questions:
    1) Do you like warm places
    2) Do you like the beach?
    # 3) Do you want to fly?
    4) Do you like hiking?

    Destinations:
    Beach- (warm-) fly- Spain
    Beach- OOB
    Beach- Hiking- Acedia


    warm- fly- Egypt
    warm- hiking- Redwoods

    
"""

fly = input("Do you want to fly? (yes or no) ")
beach = input("Do you like beaches? (yes or no)")
hiking = input("Do you like hiking? (yes or no)")

if (fly != 'yes' or fly != 'no') or (beach != 'yes' or beach != 'no') or (hiking != 'yes' or hiking != 'no'):
     print("use better inputs next time buddy")

if fly == 'yes':
    if beach == 'yes' and hiking =='no':
        print("Spain\nHawaii")
    elif beach == 'no' and hiking == 'yes':
        print("Mount Everest\nSweeden")
    elif beach == 'yes' and hiking == 'yes':
        print("Jamacia\nLycian Way in Turkey")
    else:
        print("Greenland\nU.K.")

else:
    if beach == 'yes' and hiking =='no':
        print("Old Orchard\nOuter banks")
    elif beach == 'yes' and hiking == 'yes':
        print("Acadia\nPresumpscot River Preserve")
    elif beach == 'no' and hiking == 'yes':
         print("Killington, VT\nMount Washington")
    else:
         print("Boston\nNYC")


    
