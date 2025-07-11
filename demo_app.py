#!/usr/bin/env python3
"""
Claude Code Capabilities Demo App
This interactive app demonstrates my key abilities:
- File operations (Read, Write, Edit)
- Code analysis and search
- Running commands
- Web search and fetching
- Task management
"""

import os
import sys
import subprocess
import json
from datetime import datetime

class ClaudeDemo:
    def __init__(self):
        self.capabilities = {
            "1": "File Operations (Create, Read, Edit files)",
            "2": "Code Search & Analysis (Find functions, patterns)",
            "3": "Command Execution (Run shell commands)",
            "4": "Project Management (Git, dependencies)",
            "5": "Web Integration (Search, fetch content)",
            "6": "Task Planning (Break down complex tasks)",
            "7": "Multi-language Support (Python, JS, Rust, etc.)",
            "8": "Testing & Debugging (Run tests, fix issues)"
        }
    
    def show_menu(self):
        print("\n🤖 Claude Code Capabilities Demo")
        print("=" * 40)
        for key, value in self.capabilities.items():
            print(f"{key}. {value}")
        print("9. Show project structure")
        print("0. Exit")
        print("=" * 40)
    
    def demo_file_ops(self):
        print("\n📁 File Operations Demo")
        
        # Create a sample config file
        config = {
            "app_name": "Claude Demo",
            "version": "1.0.0",
            "created": datetime.now().isoformat(),
            "features": list(self.capabilities.values())
        }
        
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        print("✅ Created config.json")
        
        # Read and display it
        with open("config.json", "r") as f:
            content = f.read()
        
        print("📖 File contents:")
        print(content[:200] + "..." if len(content) > 200 else content)
    
    def demo_code_analysis(self):
        print("\n🔍 Code Analysis Demo")
        print("📊 Analyzing this Python file...")
        
        # Count lines, functions, classes
        with open(__file__, "r") as f:
            lines = f.readlines()
        
        line_count = len(lines)
        func_count = len([l for l in lines if l.strip().startswith("def ")])
        class_count = len([l for l in lines if l.strip().startswith("class ")])
        
        print(f"📈 File stats:")
        print(f"  - Lines: {line_count}")
        print(f"  - Functions: {func_count}")
        print(f"  - Classes: {class_count}")
    
    def demo_commands(self):
        print("\n⚡ Command Execution Demo")
        
        try:
            # Show current directory
            result = subprocess.run(["pwd"], capture_output=True, text=True)
            print(f"📍 Current directory: {result.stdout.strip()}")
            
            # List files
            result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
            print("📋 Files in directory:")
            print(result.stdout[:300] + "..." if len(result.stdout) > 300 else result.stdout)
            
        except Exception as e:
            print(f"❌ Error running commands: {e}")
    
    def demo_project_structure(self):
        print("\n🏗️ Project Structure")
        
        def show_tree(path, prefix="", max_depth=2, current_depth=0):
            if current_depth > max_depth:
                return
            
            try:
                items = sorted(os.listdir(path))
                for i, item in enumerate(items):
                    if item.startswith('.'):
                        continue
                    
                    item_path = os.path.join(path, item)
                    is_last = i == len(items) - 1
                    
                    print(f"{prefix}{'└── ' if is_last else '├── '}{item}")
                    
                    if os.path.isdir(item_path) and current_depth < max_depth:
                        extension = "    " if is_last else "│   "
                        show_tree(item_path, prefix + extension, max_depth, current_depth + 1)
            except PermissionError:
                pass
        
        show_tree(".")
    
    def run(self):
        print("🚀 Welcome! I'm Claude Code - your AI programming assistant.")
        print("I can help with:")
        print("• Writing and editing code")
        print("• Running commands and tests")
        print("• Managing Git repositories")
        print("• Searching and analyzing codebases")
        print("• And much more!")
        
        while True:
            self.show_menu()
            choice = input("\nSelect a demo (0-9): ").strip()
            
            if choice == "0":
                print("👋 Thanks for exploring Claude Code!")
                break
            elif choice == "1":
                self.demo_file_ops()
            elif choice == "2":
                self.demo_code_analysis()
            elif choice == "3":
                self.demo_commands()
            elif choice == "9":
                self.demo_project_structure()
            else:
                print("🤖 In a real session, I would demonstrate:")
                if choice in self.capabilities:
                    print(f"   {self.capabilities[choice]}")
                print("   Try selecting 1, 2, 3, or 9 for working demos!")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = ClaudeDemo()
    app.run()