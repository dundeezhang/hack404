import type { Article } from './types';

const API_BASE_URL = 'http://localhost:5000';

export const apiService = {
  async getArticles(category: string = 'general', ignore: string = '', search: string = ''): Promise<Article[]> {
    try {
      const params = new URLSearchParams();
      if (category) params.append('category', category);
      if (ignore) params.append('ignore', ignore);
      if (search) params.append('search', search);

      const response = await fetch(`${API_BASE_URL}/news?${params.toString()}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching articles:', error);
      return [];
    }
  },

  async searchArticles(query: string): Promise<Article[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/news?search=${encodeURIComponent(query)}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error searching articles:', error);
      return [];
    }
  }
};

