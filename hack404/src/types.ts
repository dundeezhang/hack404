export interface Article {
    imageUrl: string;
    title: string;
    author: {
        first: string;
        last: string;
    }
    date: Date;
    filters: string[];
}

export interface ApiCall {
    articles: Article[];
}