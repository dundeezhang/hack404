import { ApiCall } from '../types';

const API_BASE_URL = 'http://locahost:5000/api';

export const apiService = {
    async getArticles(): Promise<ApiCall[]> {
        try {
            const response = await fetch(`${API_BASE_URL}/articles`);
            if(!response.ok) {
                throw new Error('Failed to fetch articles');
            }
        }
    }
}


