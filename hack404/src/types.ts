export interface Article {
  url: string;
  imageUrl: string;
  title: string;
  author: string;
  date: string;
  filters: string[];
}

export interface ApiCall {
  articles: Article[];
}
