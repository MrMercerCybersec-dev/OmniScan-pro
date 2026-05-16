import sys
import argparse
import subprocess
import json
from datetime import datetime
import ollama

# Attempt Tkinter importing gracefully for headless servers running CLI mode
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

BANNER = r"""
   ____  __  __ _   _ ___ ____   ____    _    _   _        ____  ____   ___  
  / __ \|  \/  | \ | |_ _/ ___| / ___|  / \  | \ | |      |  _ \|  _ \ / _ \ 
 | |  | | |\/| |  \| | | \___ \| |     / _ \ |  \| |_____ | |_) | |_) | | | |
 | |__| | |  | | |\  | |  ___) | |___ / ___ \| |\  |_____||  __/|  _ <| |_| |
  \____/|_|  |_|_| \___| |____/ \____/_/   \_\_| \_|      |_|   |_| \_\\___/ 
             >> Autonomous Multi-Language Security Orchestrator <<
"""

class OmniScanProEngine:
    def __init__(self, target=None, model_name="llama3"):
        self.target = target
        self.model = model_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.aggregated_logs = ""
        self.ai_analysis = ""

    def _execute_module(self, cmd, module_name, timeout=300):
        """Native operational execution layer utilizing sub-process pipelines"""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            self.aggregated_logs += f"\n--- {module_name.upper()} WRAPPER OUTPUT ---\n{result.stdout}\n"
            if result.stderr and result.returncode != 0:
                self.aggregated_logs += f"[{module_name} Notice]: {result.stderr}\n"
        except subprocess.TimeoutExpired:
            self.aggregated_logs += f"\n[!] {module_name} error: Module execution timed out.\n"
        except FileNotFoundError:
            self.aggregated_logs += f"\n[!] {module_name} error: Required dependency binary '{cmd[0]}' missing.\n"
        except Exception as e:
            self.aggregated_logs += f"\n[!] {module_name} unexpected failure: {e}\n"

    def run_reconnaissance(self):
        """Orchestrates passive asset mapping and active network probes"""
        if not self.target: return
        self._execute_module(["whois", self.target], "Whois Passive Footprint")
        self._execute_module(["nmap", "-sV", "--script=vulners", self.target], "Nmap Infrastructure Audit")
        self._execute_module(["nikto", "-h", self.target, "-Tuning", "1,2,3,b"], "Nikto Web Application Scan")

    def run_go_tracer(self):
        """Triggers the compiled high-speed Go routing module"""
        if not self.target: return
        # Calls our custom local compiled Go binary
        self._execute_module(["./tracer", self.target], "Go Concurrency Tracer", timeout=60)

    def run_c_forensics(self):
        """Triggers the compiled low-level systems C log processing module"""
        # Calls our custom local compiled C system utility
        self._execute_module(["./forensics"], "C System Log Forensics", timeout=60)

    def process_ai_correlation(self):
        """Dispatches aggregated log states to the local air-gapped LLM layer"""
        system_prompt = (
            "You are an enterprise vulnerability correlation engine. Analyze the provided multi-tool security logs. "
            "Examine network structure patterns, cryptographic configurations, web flaws, and system alerts. "
            "Synthesize these findings into a strict Markdown report containing three definitive sections: "
            "1. Core Executive Assessment, 2. Correlated Critical Flaws, 3. Strategic Mitigation Blueprints."
        )
        full_prompt = f"{system_prompt}\n\n[Collected System Telemetry Data]:\n{self.aggregated_logs}"
        
        try:
            response = ollama.generate(model=self.model, prompt=full_prompt)
            self.ai_analysis = response['response']
        except Exception as e:
            self.ai_analysis = f"AI Generation dropped due to local Ollama daemon connection error: {e}"

    def write_report_to_disk(self):
        """Commits audit data and intelligence analysis findings to local Markdown files"""
        filename = f"report_{self.timestamp}.md"
        with open(filename, "w") as report_file:
            report_file.write(f"# Comprehensive Security Profile: {self.target}\n")
            report_file.write(f"Generated Audit Window: {self.timestamp}\n\n")
            report_file.write("## 🧬 Local Intelligence Findings\n")
            report_file.write(self.ai_analysis)
            report_file.write("\n\n## 📋 Raw Ingested System Telemetry Logs\n```text\n")
            report_file.write(self.aggregated_logs)
            report_file.write("\n```\n")
        return filename

# --- THE UNIFIED GUI DESKTOP MANAGEMENT CONSOLE LAYER ---
def start_graphical_interface():
    if not GUI_AVAILABLE:
        print("[!] Error: Tkinter graphic context libraries are unavailable on this environment.")
        sys.exit(1)

    root = tk.Tk()
    root.title("OmniScan-Pro Security Control Console")
    root.geometry("850x650")
    root.configure(bg="#121212")

    # Styling Elements
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#121212", foreground="#ffffff")
    style.configure("TButton", background="#222222", foreground="#ffffff", borderwidth=1)
    style.map("TButton", background=[("active", "#333333")])

    # Top Frame Scope Components
    top_frame = tk.Frame(root, bg="#121212")
    top_frame.pack(pady=10, fill=tk.X, px=20 if hasattr(tk, 'px') else 10)
    
    ttk.Label(top_frame, text="Target Network Boundary Scope (Domain/IP): ", font=("Courier", 11)).pack(side=tk.LEFT)
    target_input = ttk.Entry(top_frame, width=40, font=("Courier", 11))
    target_input.pack(side=tk.LEFT, px=5 if hasattr(tk, 'px') else 5)

    # Output Feed Console Box
    console_box = scrolledtext.ScrolledText(root, width=95, height=27, bg="#1a1a1a", fg="#33ff33", font=("Courier", 10), insertbackground="white")
    console_box.pack(pady=10)
    console_box.insert(tk.END, BANNER + "\n[+] Console Core Active. Ready for input parameter registration...\n")

    def execute_ui_pipeline():
        target = target_input.get().strip()
        if not target:
            messagebox.showerror("Validation Error", "Please establish a valid infrastructure destination target.")
            return

        console_box.insert(tk.END, f"\n[*] Registering target parameter scope: {target}\n")
        console_box.insert(tk.END, "[*] Triggering native Go routing and C forensics analysis engines...\n")
        root.update()

        engine = OmniScanProEngine(target=target)
        
        # Run binary utilities
        engine.run_go_tracer()
        engine.run_c_forensics()
        console_box.insert(tk.END, "[+] Core telemetry loops running successfully.\n[*] Starting deep active framework scanning protocols...\n")
        root.update()

        # Run active scan engines
        engine.run_reconnaissance()
        console_box.insert(tk.END, "[+] Data scanning tasks complete. Transferring profile to local LLM context...\n")
        root.update()

        # Generate local AI summaries
        engine.process_ai_correlation()
        saved_file = engine.write_report_to_disk()
        
        console_box.insert(tk.END, f"\n=== LOCAL AI INTELLIGENCE SUMMARY ===\n{engine.ai_analysis}\n")
        console_box.insert(tk.END, f"\n[+] Production audit files saved successfully to disk as: {saved_file}\n")
        root.update()

    ttk.Button(top_frame, text="LAUNCH FULL PLATFORM AUDIT", command=execute_ui_pipeline).pack(side=tk.LEFT, px=10 if hasattr(tk, 'px') else 10)
    root.mainloop()

# --- ENTRY POINT MANAGEMENT CLI DISPATCHER ---
if __name__ == "__main__":
    print(BANNER)
    
    # Check for parameter context inputs to choose between running CLI or GUI modes
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="OmniScan-Pro Security Framework")
        parser.add_argument("--target", help="Specify destination assessment scope (IP or Domain)")
        parser.add_argument("--cli", action="store_true", help="Force headless command line terminal mode execution")
        args = parser.parse_args()
        
        if args.cli and args.target:
            print(f"[*] Starting head-less audit orchestration against target context: {args.target}")
            cli_engine = OmniScanProEngine(target=args.target)
            
            cli_engine.run_go_tracer()
            cli_engine.run_c_forensics()
            cli_engine.run_reconnaissance()
            
            cli_engine.process_ai_correlation()
            output_report = cli_engine.write_report_to_disk()
            
            print("\n=== ENGINE ANALYSIS STRATEGY REPORT ===")
            print(cli_engine.ai_analysis)
            print(f"\n[+] Processing pipeline complete. Audit records committed to: {output_report}")
        else:
            parser.print_help()
    else:
        # Defaults straight to launching desktop management console window if no flag context arguments are explicitly passed
        start_graphical_interface()
