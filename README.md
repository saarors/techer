# 🎓 techer – מורה פרטי מקומי בעברית

מורה פרטי לכל מקצוע (מתמטיקה, פיזיקה, כימיה, ביולוגיה, מדעי המחשב, אנגלית, היסטוריה, ספרות ועוד),
עם ממשק ווב בעברית. רץ מקומית על המחשב עם Ollama והמודל DictaLM 3.0 – בלי ענן ובלי עלות.

## התקנה
1. התקן Ollama (גרסה עדכנית): https://ollama.com
2. הורד את המודל:
   `ollama pull hf.co/dicta-il/DictaLM-3.0-Nemotron-12B-Instruct-GGUF:Q4_K_M`
3. `python -m venv .venv`
4. הפעלה: `.venv\Scripts\Activate.ps1` (Windows) או `source .venv/bin/activate` (Mac/Linux)
5. `pip install -r requirements.txt`
6. `uvicorn app:app --reload`
7. פתח http://localhost:8000

## הערות
- כל מקצוע שומר היסטוריית שיחה נפרדת בדפדפן (localStorage).
- המודל דורש בערך 8GB זיכרון פנוי. אם יש בעיות הרצה, עדכן את Ollama.
- להוספת מקצוע: ערוך את `subjects.py`.