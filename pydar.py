'''
little endian

https://stackoverflow.com/questions/39840400/view-double-variable-in-memory
'''


def combine(byte_array, target=int):
    '''
    TODO
    '''
    
    if target == str:
        result = ''
    elif target == int:
        result = 0
    elif target == float:
        result = 0
        
        sign     = 0
        exponent = 0
        mantissa = 0
        
        if len(byte_array) < 8:
            print('Not enough bytes to convert array to float/double')
            return result

    index = 0

    try:
        for byte in byte_array:
            if target == str:
                if not byte == 0: # ignore NULL for string construction
                    result += chr(byte)
                
            elif target == int:
                result += byte << 8
                index  += 1
                
            elif target == float:
                if index == 0: # parse sign and most of the exponent
                    sign     = (byte & 128) >> 7
                    exponent = (byte & 127) << 8
                
                elif index == 1: # finish parsing exponent and the first 4 bits of the mantissa
                    exponent += byte >> 4
                    mantissa = (byte & 15) << 48
                    
                elif not index == 7:
                    mantissa += byte
                
                elif index == 8:
                    pass
                
    except TypeError:
        if target == str:
            result = chr(byte_array)
        
        elif target == int or target == float:
            result = byte_array
            
    return result


if __name__ == '__main__':
    file_stuff = {}
    
    with open('0-0-0-0.las', 'rb') as las:
        content = las.read()
    
    content = bytearray(content)
    
    file_stuff['File_Signature'] = combine(content[0:4], target=str)
    file_stuff['File_Source_ID'] = combine(content[4:6])
    file_stuff['Global_Encoding'] = combine(content[6:8])
    file_stuff['Project_ID_GUID_data_1'] = combine(content[8:12])
    file_stuff['Project_ID_GUID_data_2'] = combine(content[12:14])
    file_stuff['Project_ID_GUID_data_3'] = combine(content[14:16])
    file_stuff['Project_ID_GUID _data_4'] = combine(content[16:24])
    file_stuff['Version_Major'] = combine(content[24])
    file_stuff['Version_Minor'] = combine(content[25])
    file_stuff['System_Identifier'] = combine(content[26:58], target=str)
    file_stuff['Generating_Software'] = combine(content[58:90])
    file_stuff['File_Creation_Day_of_Year'] = combine(content[90:92])
    file_stuff['File_Creation_Year'] = combine(content[92:94])
    file_stuff['Header Size'] = combine(content[94:96])
    file_stuff['Offset_to_point_data'] = combine(content[96:100])
    file_stuff['Number_of_Variable_Length_Records'] = combine(content[100:104])
    file_stuff['Point_Data_Record_Format'] = combine(content[104])
    file_stuff['Point_Data_Record_Length'] = combine(content[105:107])
    file_stuff['Legacy_Number_of_point_records'] = combine(content[107:111])
    file_stuff['Legacy_Number_of_points_by_return'] = combine(content[111:131])
    file_stuff['X_scale_factor'] = content[131:139]
    file_stuff['Y_scale_factor'] = combine(content[139:147])
    file_stuff['Z_scale_factor'] = combine(content[147:155])
    file_stuff['X_offset_double'] = combine(content[155:163])
    file_stuff['Y_offset_double'] = combine(content[163:171])
    file_stuff['Z_offset_double'] = combine(content[171:179])
    #Max X double 8 bytes *
    #Min X double 8 bytes *
    #Max Y double 8 bytes *
    #Min Y double 8 bytes *
    #Max Z double 8 bytes *
    #Min Z double 8 bytes *
    #Start of Waveform Data Packet Record Unsigned long long 8 bytes *
    #Start of first Extended Variable Length
    #Record
    #unsigned long long 8 bytes *
    #Number of Extended Variable Length
    #Records
    #unsigned long 4 bytes *
    #Number of point records unsigned long long 8 bytes *
    #Number of points by return 
    
    import pprint
    
    pprint.pprint(file_stuff)
    print('Done')
    
    
    
    
