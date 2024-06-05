import streamlit as st
import streamlit.components.v1 as com
with open("style_fiturTTS.css") as source:
    design=source.read()
com.html(f"""
         <body>
         <style>
         {design}
         <style>
    <header>
        <div class="title">
            <h3 class="title-text">Text to Speech Converter</h3>
            <div class="search-bar">
                <input type="text" placeholder="Search in site" name="search-box">
                <i class="fas fa-search"></i>
            </div>
            
        </div>
    </header>
    
    <div class="TTSflex-container">
        <aside>
            <div class="Sidebar-navigation">
                <ul>
                    <li><a href="fiturTTS.blade.php">Text to Speech</a></li>
                    <li><a href="fiturSummarize.blade.php">Summarize</a></li>
                    <li><a href="fiturTranslate.blade.php">Translate Languages</a></li>
                    <li><a href="fiturSearchPaper.blade.php">Search Paper</a></li>
                    <li><a href="fiturPublishing.blade.php">Publishing</a></li>
                </ul>
            </div>
       </aside>
    
       <main>
            <div class="Converter">
                <div class="convert">
                    <h1 class="title-TTS">Text to Speech Converter</h1>
                    <input type="file" placeholder="Enter file to convert">
                    <div class="button-upload">
                        <button class="btn">Upload PDF</button>

                    </div>

                </div>
                
                
                <div class="Display-PDF">
                    <div class="button-converter">
                        <button class="button-generate">Generate Conclusion</button>
                        <button class="button-speech">Convert to Speech</button>
                    </div>

                    <div class="card-display">
                        <div class="text-display">
                            <p class="text-explanation">Text Explanation</p>
                        </div>
                        <div class="text-speech">
                            <h3 class="title-text-speech">Display Text</h3>
                            <p class="display-text-speech">Text that is read</p>
                        </div>

                    </div>

                </div>
    
            </div>
    
       </main>

    </div>
   

    
</body>""", height=600)