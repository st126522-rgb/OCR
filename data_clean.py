import re
from random import *
import datasetCreate as dc

unicode_dev_set_string=''
def font_glyph_check(font):    
    #consonants and vowels with diacritics
    dev_chars=['\u094D','म', 'झ', 'ट', 'ऽ', 'ी', 'ओ', 'ु', 'ऐ', 'क', 'घ', 'ञ', 'छ', 'व', 'स', 'ज', 'ौ', 'ब', 'ू', 'ध', 'ए', 'थ', 'च', 'ण', 'भ', 'ा', 'उ', 'ॉ', 'र', 'त', 'ॅ', 'ढ', 'ग', 'ष', 'ल', 'ह', 'य', 'ऩ', 'प', 'ई', 'ि', 'न', 'औ', 'ृ', 'ठ', 'अ', 'इ', 'ै', 'े', 'द', 'ः', 'ड', 'श', 'ो', 'आ', 'ख', 'ं', 'ऱ', 'ऋ', 'ँ', 'फ', 'ङ', 'ऊ']
    
    #ligatures top 40 in terms of frequency of collected data (obtained from datastats.ipynb)
    conjuncts_top_40=['प्र', 'न्त', 'त्य', 'र्न', 'स्त', 'न्छ', 'त्र', 'क्ष', 'न्द', 'स्व', 'व्य', 'न्न', 'र्द', 'द्ध', 'स्थ', 'त्त', 'क्त', 'न्य', 'र्थ', 'र्म', 'ष्ट', 'त्म', 'र्व', 'क्र', 'म्म', 'र्य', 'स्क', 'ध्य', 'र्छ', 'र्ण', 'ल्य', 'र्ष', 'र्त', 'र्क', 'फ्न', 'म्र', 'म्प', 'ग्र', 'ण्ड']


    sorted_char_list = sorted(dev_chars, key=lambda char: ord(char[0]))
    merged_list = sorted_char_list + conjuncts_top_40

    additional_characters = '०१२३४५६७८९,,?।-' #digits and punctuations
    characters_to_remove = 'ऩऱऽॅॉ' 
    # Create the final string
    final_string = ''.join(merged_list) + additional_characters
    print(final_string)
    # Remove specified characters
    # final_string = re.sub(f'[{re.escape(characters_to_remove)}]', '', final_string)
    # all_ligature1='ज्यज्ञल्लम्बश्रर्जर्गन्धध्वन्थश्वद्यत्वर्धद्वश्यत्पक्यग्नल्नश्चस्पल्पक्नस्यङ्कख्यख्नस्टट्टष्णक्कस्नप्तञ्चब्दञ्जर्शर्टच्चस्रच्छग्यस्मक्छष्ठन्टम्यद्दम्भर्चर्रर्फन्मत्कत्सग्छद्रभ्यर्भड्नष्पथ्यट्यक्दब्रम्झल्दर्सक्लग्द'
    # all_lig2='च्यक्सल्छल्टर्खण्णन्सढ्नश्नङ्खह्रच्नल्मप्यन्डम्तर्बट्नल्कह्यष्कष्यर्डन्जत्नझ्नब्यश्लर्लर्पप्नज्नभ्रक्टढ्दम्नद्भट्रग्लप्पण्टब्बम्लख्दफ्रख्छप्लम्कड्कब्धज्वग्गह्मज्जन्वङ्घस्लन्कम्सठ्यस्सड्दड्यड्रग्थल्तन्चम्व'
    # all_lig3='र्घल्सथ्रज्दक्वट्छस्दथ्वफ्यब्लद्मस्बह्वध्नज्रम्दस्फछ्यल्फझ्यण्यट्सम्हद्घब्जठ्ठढ्यप्टल्थव्रस्छम्धऱ्यड्डण्ठट्वच्दट्कफ्टम्चत्थठ्नख्तङ्तढ्छड्छफ्लल्झख्रघ्नप्ठक्थप्दट्दप्सल्हल्डट्ठग्मत्लल्चफ्तझ्दन्हज्छड्ढ'
    # all_lig4='ख्खश्मध्दध्रन्लङ्मद्गङ्लख्थन्पम्गय्यल्ठप्कच्कन्झप्वठ्दव्दऩ्छग्वख्वत्दग्धब्नब्सड्थट्पह्लन्ठघ्यङ्सन्फज्मध्छद्कप्चर्हष्मश्कत्खझ्छम्छद्नस्खल्बल्वह्दम्जक्मम्फल्गढ्थन्रड्पप्छष्रङ्दत्छड्गछ्मल्जक्जल्खघ्रद्लव्धङ्यब्वञ्छर्झम्टट्मष्चह्तक्चघ्वङ्ङड्तष्तक्खछ्नस्चज्थर्इन्बफ्फङ्नद्बङ्रभ्लस्जश्पग्डव्वष्फट्फश्तग्जछ्दट्लद्हव्हफ्वभ्वझ्वप्थन्उङ्छच्वङ्टन्भथ्नन्घर्ङल्भत्गग्शब्छड्फक्ढट्बम्घन्१ग्णञ्झथ्बच्थछ्रर्ईह्नड्सक्डक्झल्रग्भफ्ठट्थग्सष्वक्शग्चत्अय्लह्कज्बण्झप्खच्लद्सख्लश्शह्णड्ङद्छग्६ड्चऩ्नल्६श्टच्५च्पग्कऩ्यड्मव्बभ्नच्डफ्सम्ठक्पट्तज्कछ्छध्लक्गच्तक्धन्शञ्कन्खङ्फट्जप्जब्घन्गर्उभ्सछ्तध्चग्ऐझ्थछ्टड्भऩ्तञ्सह्चघ्घच्हब्डय्टस्हस्डग्एब्भङ्शझ्लग्इभ्दग्बङ्बश्सज्लध्थन्एङ्थठ्छन्५ञ्रड्बत्भम्ण'
    preeti_final_string='''F+MccfOO{ppmCPP]cf]cf}svu3ªr5hem`67890ftybwgkkmaedo/njzif;xlfL'"[]}f]f}k|GtTog{:tG5qIfGb:jJoGgb{4:yQQmGoy{d{i6Tdj{qmDdo{:sWo5{0f{Ën\oif{t{s{km\gd|Dku|08)!@#$%^&*(,,<.-'''
    all_lig_preeti = r'''Ho1n\nDa>h{u{GwWjGyZjBTjw{åZoTkSoUgn\gZr:kn\kSg:oÍVoVg:6§i0fSs:gKt~rAb~hz{6{Rr;|R5¡:dS5i7G6Do2Der{/{km{GdTsT;U5›Eoe{8\gikYo6\oSba|Demn\b;{SnUbRoS;n\5n\6v{00fG;9\gZgÎx|Rgn\dKoG8Dta{6\gn\sXoisio8{GhTgem\gAoZnn{k{KgHge|S69\bDgb\e6«UnKk06AaDnVbk|mV5KnDs8\sAwHjUuXdHhGj‹:nGsD;7\o:;8\b8\o8«Uyn\tGrDj3{n\;y|HbSj6\5:bYjkm\oAnß:aXjWgh|Db:km5\on\kmem\o0o6\;Dx¢Ah¶9\oK6n\yj|:5Dwऱ\o•076\jRb6\skm\6DrTy7\gVtª\t9\58\5km\nn\emv|£gK7SyKb6\bK;n\xn\8ÝUdTnn\rkm\tem\bGxH5°VvZdWb„Gnª\db\uª\nVyGkDuo\on\7KsRsGemKj7\bJbऩ\5UjVjTbUwAgA;8\y6\kXnG7£oª\;GkmHdW5b\sKrx{idZsTvem\5D5b\g:vn\an\jXbDhSdDkmn\u9\yg|8\kK5if|ª\bT58\u5\dn\hShn\v3|b\nJwª\oAj~5em{D66\dirXtSr£jª\ª8\titSv5\g:rHyl/Gakm\kmª\gb\aª|En:hZkU8Jjikm6\kmZtUh5\b6\nb\xJxkm\jEjem\jKyg'ª\5Rjª\6GeYgG3ª{n\eTuUzA58\kmS96\aD3G!U0f~emYaRy5|/LXg8\;S8Semn|Uekm\76\yU;ijSzUrto\nXsHa0emKvRnb\;VnZzX0f8\ªb\5U^8\rऩ\gn\^Z6R%RkUsऩ\o8\dJaEgR8km\;D7Sk6\tHs5\5WnSuRtSwGz~sGvª\km6\hKhA3Gu?E;5\tWru}em\y5\68\eऩ\t~;Xr£3RxA8o\6:x:8u]Aeª\zem\nluEbUaª\aZ;HnWyg]ª\y7\5G%`|8\aTeD0f'''

    #checking ligature rendering for all fonts
    unicode_dev_set_string=final_string
    dc.render_text(r"test_images\sag_test.png",font,preeti_final_string)

def remove_non_dev(data_line):
   
    pattern = r'[^\u0900-\u097F,?\s]'  # Define a pattern to remove non-Devanagari characters and whitespace
    data_line = re.sub(pattern, ' ', data_line.strip())    
    data_line=data_line.replace("़", "") #replacing the nukta grapheme as it is not being translated to preeti

    # if len(data_line)<30: return ""    
    # return data_line

# Open the input file for reading
def clean_text_file(raw_deva_path,output_path):
    
    with open(raw_deva_path, "r", encoding="utf-8") as read_file:
        for line in read_file:
            refined_string = remove_non_dev(line)
            if refined_string != "":
                collected_refined_data.append(refined_string+'\n')

    print(f'This is the length of the refined list: {len(collected_refined_data)}')
    # Filter out empty lines 
    collected_refined_data = list(filter(None, collected_refined_data))
    # Write the filtered lines to the output file
    output_file_path = output_path
    with open(output_file_path, "w", encoding='utf-8') as write_file:
        
        for line in collected_refined_data:
            write_file.write(f'{line}')




def segregate_complexity():
    seed(42)  # Set the seed for reproducibility
    halanta = "\u094D"
    dev_chars = ['\u094D','म', 'झ', 'ट', 'ऽ', 'ी', 'ओ', 'ु', 'ऐ', 'क', 'घ', 'ञ', 'छ', 'व', 'स', 'ज', 'ौ', 'ब', 'ू', 'ध', 'ए', 'थ', 'च', 'ण', 'भ', 'ा', 'उ', 'ॉ', 'र', 'त', 'ॅ', 'ढ', 'ग', 'ष', 'ल', 'ह', 'य', 'ऩ', 'प', 'ई', 'ि', 'न', 'औ', 'ृ', 'ठ', 'अ', 'इ', 'ै', 'े', 'द', 'ः', 'ड', 'श', 'ो', 'आ', 'ख', 'ं', 'ऱ', 'ऋ', 'ँ', 'फ', 'ङ', 'ऊ']
    conjuncts_top_40 = ['प्र', 'न्त', 'त्य', 'र्न', 'स्त', 'न्छ', 'त्र', 'क्ष', 'न्द', 'स्व', 'व्य', 'न्न', 'र्द', 'द्ध', 'स्थ', 'त्त', 'क्त', 'न्य', 'र्थ', 'र्म', 'ष्ट', 'त्म', 'र्व', 'क्र', 'म्म', 'र्य', 'स्क', 'ध्य', 'र्छ', 'र्ण', 'ल्य', 'र्ष', 'र्त', 'र्क', 'फ्न', 'म्र', 'म्प', 'ग्र', 'ण्ड']
    conjunct_pattern = re.compile(r"\w्\w")

    with open(r'txt_files\cleaned_output.txt', 'r', encoding='utf-8') as clean_output:
        data_lines = clean_output.readlines()

    common_lines = []
    complex_lines = []

    for line in data_lines:
        # Check if the line contains the halanta pattern and it's not in the top 40 conjuncts
        if halanta in line and not any(char in line for char in dev_chars):
            complex_lines.append(line)
            continue

        # Check if the line contains the conjunct pattern
        if conjunct_pattern.search(line):
            # Check if the conjuncts in the line are in the top 40 list
            conjuncts = conjunct_pattern.findall(line)
            if all(conjunct in conjuncts_top_40 for conjunct in conjuncts):
                common_lines.append(line)
            else:
                complex_lines.append(line)
        else:
            common_lines.append(line)
    shuffle(common_lines)
    shuffle(complex_lines)
    print(f'Complex lines: {len(complex_lines)} \n Simple lines: {len(common_lines)}')
    with open(r'txt_files\simple_lines.txt', 'w', encoding='utf-8') as common_file:
        common_file.writelines(common_lines)

    with open(r'txt_files\complex_lines.txt', 'w', encoding='utf-8') as complex_file:
        complex_file.writelines(complex_lines)


def get_char_metrics(dev_char):
    with open(r'txt_files\cleaned_output.txt', 'r', encoding='utf-8') as clean_output:
        data_lines = clean_output.readlines()
    dev_char_counter=0
    total_chars=0
    lines_with_char=0
    for line in data_lines:
        no_blankspace_line=line.replace(' ','')
        total_chars+=len(no_blankspace_line)
        occurance=line.count(dev_char)
        dev_char_counter+=occurance
        if occurance>0:
            lines_with_char+=1

    print(f"Total devanagari character {dev_char}  present in dataset: {dev_char_counter} ")
    print(f"Total lines with devanagari character {dev_char}  present in dataset: {lines_with_char} ")
    print(f" Character occurance % in dataset: {(dev_char_counter/total_chars)*100}% of {total_chars} characters")



if __name__=='__main__':
    input_file_path = r"txt_files\raw_webscraped_text.txt"
    output_path=r"txt_files\cleaned_output.txt"
    # segregate_complexity()
    font_glyph_check(dc.font_link_Sagarmatha)
    
    
    

