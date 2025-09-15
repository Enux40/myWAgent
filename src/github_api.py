import requests
from config import settings
from src.logger import logger


class GitHubAPI:
    def __init__(self):
        settings.validate_github_config()
        
        self.api_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {settings.GITHUB_API_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        }

    def create_repository(self, name: str, description: str = "", private: bool = False, auto_init: bool = True):
        """
        Create a new repository in the authenticated user's account.
        
        Args:
            name (str): The name of the repository
            description (str): A short description of the repository
            private (bool): Whether the repository should be private (default: False)
            auto_init (bool): Whether to initialize the repository with a README (default: True)
            
        Returns:
            dict: Repository data if successful, None if failed
        """
        url = f"{self.api_url}/user/repos"
        payload = {
            "name": name,
            "description": description,
            "private": private,
            "auto_init": auto_init,
        }
        
        try:
            response = requests.post(
                url, headers=self.headers, json=payload, timeout=10
            )
            response.raise_for_status()
            repo_data = response.json()
            logger.info(f"Repository '{name}' created successfully: {repo_data['html_url']}")
            return repo_data
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 422:
                logger.error(f"Repository name '{name}' already exists or is invalid")
            else:
                logger.error(f"HTTP error creating repository: {e} - Response: {getattr(e.response, 'text', None)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error creating repository: {e}")
        return None

    def list_repositories(self, per_page: int = 30, page: int = 1):
        """
        List repositories for the authenticated user.
        
        Args:
            per_page (int): Number of repositories per page (default: 30, max: 100)
            page (int): Page number to retrieve (default: 1)
            
        Returns:
            list: List of repository data if successful, None if failed
        """
        url = f"{self.api_url}/user/repos"
        params = {
            "per_page": min(per_page, 100),
            "page": page,
            "sort": "updated",
            "direction": "desc"
        }
        
        try:
            response = requests.get(
                url, headers=self.headers, params=params, timeout=10
            )
            response.raise_for_status()
            repos_data = response.json()
            logger.info(f"Retrieved {len(repos_data)} repositories (page {page})")
            return repos_data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error listing repositories: {e} - Response: {getattr(e.response, 'text', None)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error listing repositories: {e}")
        return None

    def get_user_info(self):
        """
        Get information about the authenticated user.
        
        Returns:
            dict: User data if successful, None if failed
        """
        url = f"{self.api_url}/user"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            user_data = response.json()
            logger.info(f"Retrieved user info for: {user_data.get('login', 'Unknown')}")
            return user_data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error getting user info: {e} - Response: {getattr(e.response, 'text', None)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error getting user info: {e}")
        return None