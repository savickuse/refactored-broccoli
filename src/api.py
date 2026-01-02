# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 9


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 13


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 21


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 26


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 27


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 32


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 39


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 43


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 44


# API module for BroccoliDB

from typing import Dict, Optional

class API:
    """RESTful API handler."""
    def __init__(self):
        self.routes = {}
    
    def register_route(self, path: str, handler):
        """Register a new route."""
        self.routes[path] = handler
    
    def handle_request(self, method: str, path: str, data: Optional[Dict] = None):
        """Handle an API request."""
        if path in self.routes:
            return self.routes[path](data or {})
        return {"error": "Not found"}, 404
    
    def get_routes(self):
        """Get all registered routes."""
        return list(self.routes.keys())

# Update 46


"""
Refactored Broccoli - Bug Fix
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}
