import pandas as pd
import glob
import os
import sys
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

print("--- SHIELD 1.0: MULTILINGUAL RISK ENGINE (DE-OBFUSCATION ACTIVE) ---")

def deobfuscate_text(text):
    """
    Normalizes 'leetspeak' characters to standard English letters.
    """
    text = str(text).lower()
    replacements = {
        '@': 'a', '4': 'a', '/\\': 'a',
        '3': 'e', '#': 'e',
        '1': 'i', '!': 'i', '|': 'i',
        '0': 'o',
        '$': 's', '5': 's', '&': 's',
        '+': 't', '7': 't'
    }
    for symbol, char in replacements.items():
        text = text.replace(symbol, char)
    return text

def translate_content(text):
    """
    1. De-obfuscates text (g@nja -> ganja)
    2. Detects language
    3. Translates to English
    """
    try:
        # STEP 1: DE-OBFUSCATE
        clean_text = deobfuscate_text(text)

        # STEP 2: DETECT
        try:
            lang = detect(clean_text)
        except LangDetectException:
            lang = 'unknown'

        # STEP 3: TRANSLATE
        # Hindi keywords that might not trigger language detection
        hindi_keywords = ['maal', 'ganja', 'dawai', 'chitta', 'samaan', 'bhai', 'bhang', 'charas', 'afim']
        needs_translation = lang != 'en' or any(k in clean_text for k in hindi_keywords)

        if needs_translation:
            try:
                translated = GoogleTranslator(source='auto', target='en').translate(clean_text)
                return translated, lang, text
            except:
                return clean_text, lang, text # Fallback to cleaned text
        else:
            return clean_text, 'en', text

    except Exception as e:
        print(f" [WARN] Processing failed: {e}")
        return text, 'error', text

def analyze_threats():
    # 1. Load latest intel - UPDATED FILENAME PATTERN
    files = glob.glob('../data/data1_*.csv')
    if not files: 
        print(" [AI] No new intel found (checked for data1_*.csv).")
        return
        
    latest_file = max(files, key=os.path.getctime)
    df = pd.read_csv(latest_file)
    
    print(f" [AI] Analyzing {len(df)} intercepts...")
    
    translated_texts = []
    langs = []
    original_texts = []

    for index, row in df.iterrows():
        raw_text = str(row['content'])
        trans, lang, orig = translate_content(raw_text)
        
        translated_texts.append(trans)
        langs.append(lang)
        original_texts.append(orig)
        
        if index % 20 == 0: print(f"  > Processed {index}/{len(df)}...")

    df['content'] = translated_texts      
    df['original_content'] = original_texts 
    df['language'] = langs                

    # 3. Apply Risk Scoring
    high_risk_keywords = [
        # Action Words
        'menu', 'shipping', 'wickr', 'signal', 'stock', 'landed', 'btc', 'crypto', 'delivery',
        # Health Hazards
        'mtp', 'abortion', 'kit', 'pills', 'steroids', 'hgh', 'testosterone', 'pharmacy', 'no prescription',
        # Substances (Clean versions of obfuscated words)
        'ganja', 'bhang', 'weed', 'charas', 'afim', 'grass', 'drug', 'coke', 'cocaine', 'heroin', 'meth', 'crystal'
    ]
    
    def calculate_threat(row):
        score = row['risk_score']
        text = str(row['content']).lower()
        
        hits = sum(k in text for k in high_risk_keywords)
        score += (hits * 12) # Increased weight for keyword matches
        
        return min(99, score)

    df['final_threat'] = df.apply(calculate_threat, axis=1)
    
    df['status'] = df['final_threat'].apply(lambda x: 'CRITICAL' if x > 80 else 'SUSPICIOUS' if x > 50 else 'LOW')
    
    output_path = latest_file.replace('.csv', '_analyzed.csv')
    df.to_csv(output_path, index=False)
    
    crit_count = len(df[df['status']=='CRITICAL'])
    print(f" [AI] Analysis Complete. {crit_count} Critical Threats identified.")

if __name__ == "__main__":
    analyze_threats()