import requests

def search_books_api(query, limit=12):
    if not query:
        return []

    # URL endpoint Open Library
    safe_query = query.replace(" ", "+")
    url = f"https://openlibrary.org/search.json?q={safe_query}&limit={limit}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        
        data = response.json()
        books = []
        
        if "docs" in data:
            for item in data["docs"]:
                title = item.get("title", "Judul Tidak Diketahui")
                authors = ", ".join(item.get("author_name", ["Penulis Tidak Diketahui"]))
                published_date = str(item.get("first_publish_year", "-"))
                
                # Ambil cover ID, lalu bentuk URL-nya
                cover_id = item.get("cover_i")
                thumbnail = ""
                if cover_id:
                    thumbnail = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"

                books.append({
                    "title": title,
                    "author": authors,
                    "synopsis": "Sinopsis tidak tersedia. (Data dari Open Library)",
                    "published_date": published_date,
                    "category": "Global Search", # Kategori default untuk hasil API
                    "cover_image": thumbnail,
                    "external_id": item.get("key", "")
                })
        return books

    except requests.exceptions.RequestException as e:
        # Error handling jika internet mati atau API down
        print(f"Error API: {e}")
        return []