#!/usr/bin/env python3
"""
Non-interactive demo of Claude Code capabilities
"""

import os
import json
from datetime import datetime

def demo_capabilities():
    print("🤖 Claude Code Capabilities Demo")
    print("=" * 50)
    
    # 1. File Operations Demo
    print("\n📁 File Operations Demo")
    config = {
        "app_name": "Claude Demo",
        "version": "1.0.0", 
        "created": datetime.now().isoformat(),
        "capabilities": [
            "File creation and editing",
            "Code search and analysis", 
            "Command execution",
            "Git integration",
            "Multi-language support"
        ]
    }
    
    with open("demo_config.json", "w") as f:
        json.dump(config, f, indent=2)
    print("✅ Created demo_config.json")
    
    # 2. Code Analysis Demo
    print("\n🔍 Code Analysis Demo")
    with open(__file__, "r") as f:
        lines = f.readlines()
    
    line_count = len(lines)
    func_count = len([l for l in lines if l.strip().startswith("def ")])
    
    print(f"📈 This file stats:")
    print(f"  - Lines: {line_count}")
    print(f"  - Functions: {func_count}")
    
    # 3. Project Structure
    print("\n🏗️ Current Project Structure:")
    try:
        files = os.listdir(".")
        for f in sorted(files):
            if not f.startswith('.'):
                print(f"  📄 {f}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n🚀 What Claude Code Can Do:")
    print("• Create and edit code in any language")
    print("• Search through large codebases")
    print("• Run tests and fix issues") 
    print("• Manage git repositories")
    print("• Integrate with development tools")
    print("• Break down complex tasks")
    print("• Work with VS Code and other editors")
    
    print("\n✨ Try asking me to:")
    print("- 'Add a new feature to this app'")
    print("- 'Fix any bugs in the code'")
    print("- 'Set up testing for this project'")
    print("- 'Optimize this code for performance'")

if __name__ == "__main__":
    demo_capabilities()