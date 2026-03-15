import sys
import os

# Add helper directory to path so we can import functions
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from functions.file_metadata.get_file_size import get_file_size
from functions.file_metadata.get_file_extension import get_file_extension
from functions.file_metadata.get_file_created_time import get_file_created_time
from functions.file_metadata.get_file_modified_time import get_file_modified_time
from functions.file_metadata.is_file_readable import is_file_readable
from functions.file_metadata.is_file_writable import is_file_writable
from functions.file_metadata.get_absolute_path import get_absolute_path
from functions.file_metadata.file_exists import file_exists
from functions.file_metadata.get_file_owner import get_file_owner
from functions.file_metadata.get_file_permissions import get_file_permissions

from unittest.mock import Mock, patch, MagicMock
import pytest


class TestFileMetadata:
    """Test suite for file metadata functions"""

    def test_get_file_size(self):
        """
        Test getting file size

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.isfile') as mock_isfile, \
             patch('os.path.getsize') as mock_size:
            mock_exists.return_value = True
            mock_isfile.return_value = True
            mock_size.return_value = 2048000
            result = get_file_size("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['size_bytes'] == 2048000
            assert result['size_kb'] == 2000.0
            assert result['size_mb'] == 1.95

    def test_get_file_extension(self):
        """
        Test extracting file extension

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = True
            result = get_file_extension("/home/user/document.pdf")
            
            assert result['path'] == "/home/user/document.pdf"
            assert result['filename'] == "document.pdf"
            assert result['extension'] == ".pdf"

    def test_get_file_extension_no_extension(self):
        """
        Test file without extension

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = True
            result = get_file_extension("/home/user/README")
            
            assert result['path'] == "/home/user/README"
            assert result['filename'] == "README"
            assert result['extension'] == "No extension"

    def test_get_file_created_time(self):
        """
        Test getting file creation time

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.getctime') as mock_getctime:
            mock_exists.return_value = True
            mock_getctime.return_value = 1609459200.0
            result = get_file_created_time("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['created_timestamp'] == 1609459200.0
            assert 'created_datetime' in result
            assert 'created_date' in result
            assert 'created_time' in result

    def test_get_file_modified_time(self):
        """
        Test getting file modification time

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.getmtime') as mock_getmtime:
            mock_exists.return_value = True
            mock_getmtime.return_value = 1640995200.0
            result = get_file_modified_time("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['modified_timestamp'] == 1640995200.0
            assert 'modified_datetime' in result
            assert 'modified_date' in result
            assert 'modified_time' in result

    def test_is_file_readable(self):
        """
        Test checking file readability

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.access') as mock_access:
            mock_exists.return_value = True
            mock_access.return_value = True
            result = is_file_readable("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['is_readable'] is True

    def test_is_file_readable_not_readable(self):
        """
        Test when file is not readable

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.access') as mock_access:
            mock_exists.return_value = True
            mock_access.return_value = False
            result = is_file_readable("/tmp/restricted.txt")
            
            assert result['path'] == "/tmp/restricted.txt"
            assert result['is_readable'] is False

    def test_is_file_writable(self):
        """
        Test checking file writeability

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.access') as mock_access:
            mock_exists.return_value = True
            mock_access.return_value = True
            result = is_file_writable("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['is_writable'] is True

    def test_is_file_writable_not_writable(self):
        """
        Test when file is not writable

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.access') as mock_access:
            mock_exists.return_value = True
            mock_access.return_value = False
            result = is_file_writable("/tmp/readonly.txt")
            
            assert result['path'] == "/tmp/readonly.txt"
            assert result['is_writable'] is False

    def test_get_absolute_path(self):
        """
        Test getting absolute path

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.abspath') as mock_abs, \
             patch('os.path.exists') as mock_exists:
            mock_abs.return_value = "/home/user/documents/file.txt"
            mock_exists.return_value = True
            result = get_absolute_path("./file.txt")
            
            assert result['original_path'] == "./file.txt"
            assert result['absolute_path'] == "/home/user/documents/file.txt"

    def test_get_absolute_path_nonexistent(self):
        """
        Test absolute path for nonexistent file

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.abspath') as mock_abs, \
             patch('os.path.exists') as mock_exists:
            mock_abs.return_value = "/home/user/nonexistent.txt"
            mock_exists.return_value = False
            result = get_absolute_path("nonexistent.txt")
            
            assert result['original_path'] == "nonexistent.txt"
            assert result['absolute_path'] == "/home/user/nonexistent.txt"

    def test_file_exists_true(self):
        """
        Test file existence check when file exists

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.isfile') as mock_isfile, \
             patch('os.path.isdir') as mock_isdir:
            mock_exists.return_value = True
            mock_isfile.return_value = True
            mock_isdir.return_value = False
            result = file_exists("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['exists'] is True
            assert result['is_file'] is True
            assert result['is_directory'] is False

    def test_file_exists_false(self):
        """
        Test file existence check when file doesn't exist

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.isfile') as mock_isfile, \
             patch('os.path.isdir') as mock_isdir:
            mock_exists.return_value = False
            mock_isfile.return_value = False
            mock_isdir.return_value = False
            result = file_exists("/tmp/nonexistent.txt")
            
            assert result['path'] == "/tmp/nonexistent.txt"
            assert result['exists'] is False
            assert result['is_file'] is False
            assert result['is_directory'] is False

    def test_file_exists_directory(self):
        """
        Test file existence check for a directory

        Args:
            None

        Returns:
            Any: Function result.
        """
        with patch('os.path.exists') as mock_exists, \
             patch('os.path.isfile') as mock_isfile, \
             patch('os.path.isdir') as mock_isdir:
            mock_exists.return_value = True
            mock_isfile.return_value = False
            mock_isdir.return_value = True
            result = file_exists("/home/user/documents")
            
            assert result['path'] == "/home/user/documents"
            assert result['exists'] is True
            assert result['is_file'] is False
            assert result['is_directory'] is True

    def test_get_file_owner(self):
        """
        Test getting file owner information

        Args:
            None

        Returns:
            Any: Function result.
        """
        mock_stat_result = Mock()
        mock_stat_result.st_uid = 501
        
        with patch('os.path.exists') as mock_exists, \
             patch('os.stat') as mock_stat, \
             patch('pwd.getpwuid') as mock_getpwuid:
            mock_exists.return_value = True
            mock_stat.return_value = mock_stat_result
            mock_getpwuid.return_value = Mock(pw_name='testuser')
            result = get_file_owner("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert result['uid'] == 501
            assert result['owner'] == 'testuser'

    def test_get_file_permissions(self):
        """
        Test getting file permissions

        Args:
            None

        Returns:
            Any: Function result.
        """
        mock_stat_result = Mock()
        mock_stat_result.st_mode = 33188  # -rw-r--r-- in octal: 0o644
        
        with patch('os.path.exists') as mock_exists, \
             patch('os.stat') as mock_stat:
            mock_exists.return_value = True
            mock_stat.return_value = mock_stat_result
            result = get_file_permissions("/tmp/test.txt")
            
            assert result['path'] == "/tmp/test.txt"
            assert 'octal' in result
            assert 'symbolic' in result
            assert 'owner_read' in result
            assert 'owner_write' in result
            assert 'owner_execute' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
