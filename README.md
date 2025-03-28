# The Daily Pulse Generator 📰🚀  

Automate your newsletter creation with ease! This tool lets you generate a custom newsletter based on the latest global news, sports, finance, and tech updates using a simple GUI.  

## 🚀 Getting Started  

Follow these steps to set up and run the repository on your local machine.  

### 📥 Clone the Repository  
First, clone the repository using Git:  

```sh
git clone https://github.com/your-username/daily-pulse-generator.git  
cd newsletter_creator 
```  

### 📦 Install Dependencies  
Ensure you have Python installed, then install the required dependencies:  

```sh
pip install -r requirements.txt  
```  

### 🔑 Set Up API Keys  
This application requires API keys for **NewsAPI** and **SerpAPI** to fetch the latest news.  

1. Create a `.env` file in the root directory.  
2. Add the following lines, replacing `your_api_key` with your actual keys:  

```plaintext
NEWS_API=your_newsapi_key  
SERP_API=your_serpapi_key  
```  

### ▶️ Run the Application  
Start the Streamlit GUI using the following command:  

```sh
streamlit run app.py  
```  

### 🎨 Customize & Generate Your Newsletter  
1. A web-based GUI will open in your browser.  
2. Use the sidebar to customize your newsletter parameters.  
3. Click the **"Create Newsletter"** button to generate a fresh newsletter.
4. Open/Host the [generated_newsletter.html](generated_newsletter.html) to read your newsletter.

## 🎯 Features  
✅ Pulls real-time news from trusted sources  
✅ User-friendly GUI for easy customization  
✅ Automatically formats the newsletter for readability  
✅ One-click newsletter generation  

## 📜 License  
This project is licensed under the MIT License.  

---

Happy automating! 🚀  
