import os
from PIL import ImageFont,ImageDraw,Image,ImageEnhance



font_link_ARAP_italic=r'fonts\003 ARAP Italic.ttf'
font_link_ganesh=r"fonts\Ganesh Regular.ttf"
font_link_aakriti=r'fonts\Aakriti Regular.ttf'
font_link_aalekh=r'fonts\Aalekh Regular.otf'#chandrabindu 
font_link_Sagarmatha=r'fonts\sagarmatha-regular.TTF'
font_link_lalit=r'fonts\Lalit-L M C C S001.000.ttf'
font_link_Ananda=r'fonts\Ananda 1 Hv Regular.otf' 
font_link_shringar=r'fonts\CV Shrinagar Regular.ttf' 

font_link_Preeti=r"fonts\preeti.TTF"
font_link_preeti_bold=r'fonts\Preeti Bold.otf'
font_link_Mangal=r"fonts\Mangal Regular.ttf"
font_link_Mangal_bold=r'fonts\Mangal Bold.ttf'
font_link_Annapurna=r"fonts\AnnapurnaSIL-Regular.ttf" 
font_link_Annapurna_bold=r'fonts\AnnapurnaSIL-Bold.ttf'
font_link_Noto_Sans_devanagari=r"fonts\NotoSansDevanagari-VariableFont_wdth,wght.ttf"
font_link_Noto_Sans_devanagari_bold=r'fonts\NotoSansDevanagari-Bold.ttf'

# Load the data from the text file
with open(r'txt_files\complex_lines.txt', 'r', encoding='utf-8') as file:
    unicode_data_cl = [line.strip() for line in file.readlines()]

with open(r'txt_files\complex_preeti.txt', 'r', encoding='utf-8') as file:
    preetiformat_data_cl = [line.strip() for line in file.readlines()]

with open(r'txt_files\simple_lines.txt', 'r', encoding='utf-8') as file:
    unicode_data_sl = [line.strip() for line in file.readlines()]

with open(r'txt_files\simple_preeti.txt', 'r', encoding='utf-8') as file:
    preetiformat_data_sl = [line.strip() for line in file.readlines()]




simple_render_list = [
    (font_link_Ananda, preetiformat_data_sl[:3000]),
    (font_link_ganesh, preetiformat_data_sl[3000:6000]),
    (font_link_aakriti, preetiformat_data_sl[6000:9000]),
    (font_link_ARAP_italic, preetiformat_data_sl[9000:12000]),
    (font_link_Sagarmatha, preetiformat_data_sl[12000:15000]),
    (font_link_lalit, preetiformat_data_sl[15000:18000]),
    (font_link_shringar, preetiformat_data_sl[18000:]),
]

# Complex Line Render List
complex_render_list = [
    (font_link_Preeti, preetiformat_data_cl[:5000]),
    (font_link_preeti_bold, preetiformat_data_cl[5000:]),
    (font_link_Mangal, unicode_data_cl[10000:13000]),
    (font_link_Mangal_bold, unicode_data_cl[13000:16000]),
    (font_link_Noto_Sans_devanagari, unicode_data_cl[16000:19000]),
    (font_link_Noto_Sans_devanagari_bold, unicode_data_cl[19000:22000]),
    (font_link_Annapurna, unicode_data_cl[22000:25000]),
    (font_link_Annapurna_bold, unicode_data_cl[25000:])  
]

print(sum)

def render_text(output_path, font_path, render_text, font_size=34, image_dpi=(300, 300)):
    try:
        # Load the font with specified layout engine
        font = ImageFont.truetype(font_path, font_size, layout_engine=ImageFont.Layout.RAQM)
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    # Calculate text dimensions
    margin = 20
    bbox = font.getbbox(render_text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Set image width proportional to text size plus border
    image_width = text_width + 2 * margin
    image_height = text_height + 2 * margin

    # Create a new white image with border
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Calculate text position to center it
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2

    # Draw the text in the center of the image
    draw.text((x, y), render_text, font=font, fill="black")

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # Save the image
    try:
        image.save(output_path, dpi=image_dpi)
    except Exception as e:
        print(f"Error saving image: {e}")

otp_path=r"test_images\sag_test.png"
render_text(otp_path,font_link_Noto_Sans_devanagari,"बताएका छन्। त्यहाँ समुद्री तटको बाटोछेउमा झुम्मिछन्")


def render_batch(render_list,unicode_data,output_dir):
    render_counter=1
    for renderset in render_list:
        font_loaded=ImageFont.truetype(font=renderset[0])
        font_name=font_loaded.getname()[0]
        font_link=renderset[0]   
        for text in renderset[1]:  
            image_name=f'{render_counter}_{font_name}'
            image_name=image_name.replace(' ','_')      
            image_path=os.path.join(output_dir,f'{image_name}.tif')
            render_text(image_path,renderset[0],text)

            # gt_filename = f'{render_counter}_{font_name}.gt.txt'
            gt_path = os.path.join(output_dir, f'{image_name}.gt.txt')
            with open(gt_path,'w',encoding='utf-8') as save_gt:            
                save_gt.write(unicode_data[render_counter-1])

            # if render_counter>=100:
            #     break
            render_counter+=1
            print(render_counter,"\t",text)
if __name__=='__main__':
    output_dir_cl=r'C:\Users\User2\Desktop\Tess\tesstrain\data\nep_cl-ground-truth'
    output_dir_sl=r'C:\Users\User2\Desktop\Tess\tesstrain\data\nep_sl-ground-truth'
    os.makedirs(output_dir_cl, exist_ok=True)
    os.makedirs(output_dir_sl, exist_ok=True)

    # render_text(r'C:\Users\User2\Desktop\VS code filesd\TesseractDefaultTestImages\1571_Preeti.tif',font_link_Preeti,"a} k|sf/sf lje]b / pTkL8gsf] cGTo ub{}")
    # render_batch(complex_render_list,unicode_data_cl,output_dir_cl)
    render_batch(simple_render_list,unicode_data_sl,output_dir_sl)
    # Create the output directory if it doesn't exist
    # output_dir = r'C:\Users\User2\Desktop\Tess\tesstrain\data\nep_dev_scrip_render_test-ground-truth'
