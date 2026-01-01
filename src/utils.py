# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 3
def helper_3(x):
    return x * 3


# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 12
def helper_12(x):
    return x * 12


# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 14
def helper_14(x):
    return x * 14


# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 33
def helper_33(x):
    return x * 33


# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 47
def helper_47(x):
    return x * 47


# Utility functions for BroccoliDB

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 52
def helper_52(x):
    return x * 52


"""
Refactored Broccoli - Performance Improvement
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    # Complex computation here
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]
