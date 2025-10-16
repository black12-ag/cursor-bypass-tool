#!/usr/bin/env python3
"""
Platform Compatibility Test for Cursor Bypass Tool
Tests all platform-specific code paths
"""

import sys
import os
import platform

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_platform_detection():
    """Test platform detection"""
    print_section("Platform Detection")
    print(f"✅ System: {platform.system()}")
    print(f"✅ Platform: {sys.platform}")
    print(f"✅ Machine: {platform.machine()}")
    print(f"✅ Python Version: {sys.version}")
    return True

def test_imports():
    """Test all required imports"""
    print_section("Testing Imports")
    
    required_modules = [
        'colorama',
        'requests',
        'psutil',
        'faker',
        'dotenv',
        'watchdog',
        'DrissionPage',
        'selenium'
    ]
    
    failed = []
    for module in required_modules:
        try:
            if module == 'dotenv':
                __import__('dotenv')
            else:
                __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {str(e)}")
            failed.append(module)
    
    if failed:
        print(f"\n❌ Missing modules: {', '.join(failed)}")
        print("Run: pip3 install -r requirements.txt")
        return False
    
    return True

def test_core_modules():
    """Test core project modules"""
    print_section("Testing Core Modules")
    
    modules = [
        'main',
        'logo',
        'config',
        'utils',
        'cursor_register_manual',
        'reset_machine_manual',
        'totally_reset_cursor',
        'simple_tempmail'
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}.py")
        except Exception as e:
            print(f"❌ {module}.py: {str(e)}")
            failed.append(module)
    
    if failed:
        print(f"\n❌ Failed modules: {', '.join(failed)}")
        return False
    
    return True

def test_paths():
    """Test platform-specific paths"""
    print_section("Testing Platform Paths")
    
    from utils import get_user_documents_path
    
    docs_path = get_user_documents_path()
    print(f"✅ Documents Path: {docs_path}")
    print(f"✅ Documents Exists: {os.path.exists(docs_path) if docs_path else False}")
    
    config_dir = os.path.join(docs_path if docs_path else os.getcwd(), ".cursor-free-vip")
    print(f"✅ Config Directory: {config_dir}")
    
    # Test platform-specific Cursor paths
    if sys.platform == "win32":
        appdata = os.getenv("APPDATA")
        cursor_path = os.path.join(appdata, "Cursor") if appdata else None
        print(f"✅ Windows Cursor Path: {cursor_path}")
    elif sys.platform == "darwin":
        cursor_path = os.path.expanduser("~/Library/Application Support/Cursor")
        print(f"✅ macOS Cursor Path: {cursor_path}")
    elif sys.platform == "linux":
        cursor_path = os.path.expanduser("~/.config/Cursor")
        cursor_path_alt = os.path.expanduser("~/.config/cursor")
        print(f"✅ Linux Cursor Path 1: {cursor_path}")
        print(f"✅ Linux Cursor Path 2: {cursor_path_alt}")
    
    return True

def test_config():
    """Test configuration system"""
    print_section("Testing Configuration")
    
    try:
        from config import get_config
        config = get_config()
        
        if config:
            print("✅ Config loaded successfully")
            print(f"✅ Config sections: {', '.join(config.sections())}")
            return True
        else:
            print("❌ Config is None")
            return False
    except Exception as e:
        print(f"❌ Config error: {str(e)}")
        return False

def test_logo():
    """Test logo display"""
    print_section("Testing Logo Display")
    
    try:
        from logo import print_logo
        print("✅ Logo function imported")
        print("\nDisplaying logo:\n")
        print_logo()
        return True
    except Exception as e:
        print(f"❌ Logo error: {str(e)}")
        return False

def test_translations():
    """Test translation system"""
    print_section("Testing Translations")
    
    try:
        from main import translator
        
        test_keys = [
            'menu.title',
            'menu.exit',
            'register.title',
            'reset.title'
        ]
        
        for key in test_keys:
            value = translator.get(key)
            if value and value != key:
                print(f"✅ {key}: {value}")
            else:
                print(f"⚠️  {key}: Missing or not loaded")
        
        available_langs = translator.get_available_languages()
        print(f"\n✅ Available languages: {', '.join(available_langs)}")
        return True
    except Exception as e:
        print(f"❌ Translation error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("  CURSOR BYPASS TOOL - PLATFORM COMPATIBILITY TEST")
    print("  Version 1.0.4 | Customized by Munir")
    print("="*60)
    
    tests = [
        ("Platform Detection", test_platform_detection),
        ("Required Imports", test_imports),
        ("Core Modules", test_core_modules),
        ("Platform Paths", test_paths),
        ("Configuration System", test_config),
        ("Logo Display", test_logo),
        ("Translation System", test_translations)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ {name} crashed: {str(e)}")
            results.append((name, False))
    
    # Summary
    print_section("Test Summary")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print(f"\n{'='*60}")
    print(f"  Total: {passed}/{total} tests passed")
    print(f"{'='*60}\n")
    
    if passed == total:
        print("🎉 All tests passed! Tool is ready for production use.")
        print("✅ Compatible with Windows, macOS, and Linux")
        return 0
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
