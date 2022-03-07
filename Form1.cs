using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Threading;
using System.Net;

namespace cmx
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            comboBox1.Items.Add("--Select-- ");
            comboBox2.Items.Add("--Select-- "); 
            comboBox3.Items.Add("--Select-- "); 
            comboBox4.Items.Add("--Select-- ");
            comboBox1.SelectedItem = "--Select-- ";
            comboBox2.SelectedItem = "--Select-- ";
            comboBox3.SelectedItem = "--Select-- ";
            comboBox4.SelectedItem = "--Select-- ";
            textBox4.Text = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile).ToString()+"\\Downloads\\";
        }

        void onouputline(object sender, DataReceivedEventArgs e)
        {
            if (comboBox1.InvokeRequired && comboBox2.InvokeRequired && !String.IsNullOrEmpty(e.Data))
            {
                if (e.Data.ToString().Contains("video only"))
                {
                    comboBox1.Invoke(new MethodInvoker(delegate () { comboBox1.Items.Add(e.Data.ToString()); }));
                }
                else if (e.Data.ToString().Contains("audio only"))
                {
                    comboBox2.Invoke(new MethodInvoker(delegate () { comboBox2.Items.Add(e.Data.ToString()); }));
                }    
            }
            else if (String.IsNullOrEmpty(e.Data))
            {
                textBox3.Invoke(new MethodInvoker(delegate () { textBox3.Text = (" Select streams"); }));
                if (comboBox2.InvokeRequired && comboBox4.InvokeRequired)
                {
                    if (comboBox2.Items.Count > 0)
                    {
                        comboBox4.Invoke(new MethodInvoker(delegate () { comboBox4.Items.Add("MP3 64K Low music"); }));
                        comboBox4.Invoke(new MethodInvoker(delegate () { comboBox4.Items.Add("MP3 320K High music"); }));
                        comboBox4.Invoke(new MethodInvoker(delegate () { comboBox4.Items.Add("M4A High music"); }));
                        comboBox4.Invoke(new MethodInvoker(delegate () { comboBox4.Items.Add("WAV High music"); }));
                        comboBox4.Invoke(new MethodInvoker(delegate () { comboBox4.Items.Add("FLAC 24 bit Studio music"); }));
                    }
                        
                }
            }
        }
        void captn(object sender, DataReceivedEventArgs e)
        {
            if (comboBox3.InvokeRequired && !String.IsNullOrEmpty(e.Data))
            {
                if (e.Data.ToString().Contains("json3"))
                {
                    comboBox3.Invoke(new MethodInvoker(delegate () { comboBox3.Items.Add(e.Data.ToString()); }));
                }
            }
        }
        void data_adder(object sender, DataReceivedEventArgs e)
        {
            if (textBox2.InvokeRequired && !String.IsNullOrEmpty(e.Data))
            {
                textBox2.Invoke(new MethodInvoker(delegate () { textBox2.Text+="\r\n"+(e.Data.ToString()); }));
            }
        }

        void thumb(object sender, DataReceivedEventArgs e)
        {
            if (pictureBox1.InvokeRequired && !String.IsNullOrEmpty(e.Data))
            {
                pictureBox1.Invoke(new MethodInvoker(delegate () {  pictureBox1.LoadAsync(e.Data.ToString()); }));
            }
        }

        void realtime(object sender, DataReceivedEventArgs e)
        {
            if (textBox3.InvokeRequired && !String.IsNullOrEmpty(e.Data))
            {
                textBox3.Invoke(new MethodInvoker(delegate () { textBox3.Text=(e.Data.ToString()); }));
            }
            else if (String.IsNullOrEmpty(e.Data))
            {
                textBox3.Invoke(new MethodInvoker(delegate () { textBox3.Text = (" Download Complete"); }));                
            }
        }
        void launch()
        {
            Process process = new Process();
            process.StartInfo.FileName = "yt-dlp_x86.exe";
            process.StartInfo.Arguments = "-F "+textBox1.Text;
            process.StartInfo.UseShellExecute = false;
            process.EnableRaisingEvents = true;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.OutputDataReceived += new DataReceivedEventHandler(onouputline);

            process.Start();
            process.BeginOutputReadLine();
            process.WaitForExit();
        }
        void caption()
        {
            Process process = new Process();
            process.StartInfo.FileName = "yt-dlp_x86.exe";
            process.StartInfo.Arguments = "--list-subs " + textBox1.Text;
            process.StartInfo.UseShellExecute = false;
            process.EnableRaisingEvents = true;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            //process.OutputDataReceived += new DataReceivedEventHandler(captn);
            process.Start();
            string output = process.StandardOutput.ReadToEnd();
            //process.BeginOutputReadLine();
            process.WaitForExit();
            //textBox2.Text = output;
            if (textBox2.InvokeRequired && !String.IsNullOrEmpty(output))
            {
                textBox2.Invoke(new MethodInvoker(delegate () { textBox2.Text = output; }));
            }
        }
        void data()
        {
            Process process = new Process();
            process.StartInfo.FileName = "yt-dlp_x86.exe";
            process.StartInfo.Arguments = "--get-duration --get-title --get-description " + textBox1.Text;
            process.StartInfo.UseShellExecute = false;
            process.EnableRaisingEvents = true;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.OutputDataReceived += new DataReceivedEventHandler(data_adder);
            process.Start();
            process.BeginOutputReadLine();
            process.WaitForExit();
        }
        void progress(string output)
        {
            Process process = new Process();
            process.StartInfo.FileName = "yt-dlp_x86.exe";
            process.StartInfo.Arguments = output;
            process.StartInfo.UseShellExecute = false;
            process.EnableRaisingEvents = true;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.OutputDataReceived += new DataReceivedEventHandler(realtime);

            process.Start();
            process.BeginOutputReadLine();
            process.WaitForExit();
        }
        void thdler()
        {
            Process process = new Process();
            process.StartInfo.FileName = "yt-dlp_x86.exe";
            process.StartInfo.Arguments = "--get-thumbnail "+textBox1.Text;
            process.StartInfo.UseShellExecute = false;
            process.EnableRaisingEvents = true;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.OutputDataReceived += new DataReceivedEventHandler(thumb);

            process.Start();
            process.BeginOutputReadLine();
            process.WaitForExit();
        }
        public void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length == 0)
            {
                MessageBox.Show("Enter Valid URL", "ytdl", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox1.Focus();
            }
            else if (textBox1.Text.Length != 0)
            {
                comboBox1.Items.Clear();
                comboBox2.Items.Clear();
                comboBox3.Items.Clear();
                comboBox4.Items.Clear();
                textBox2.Clear();
                comboBox1.Items.Add("--Select-- ");
                comboBox2.Items.Add("--Select-- ");
                comboBox3.Items.Add("--Select-- ");
                comboBox4.Items.Add("--Select-- ");
                comboBox1.SelectedItem = "--Select-- ";
                comboBox2.SelectedItem = "--Select-- ";
                comboBox3.SelectedItem = "--Select-- ";
                comboBox4.SelectedItem = "--Select-- ";
                textBox3.Text = " [Loading...]";
                
                Thread childThread = new Thread(launch);
                childThread.Start();
                Thread threadcattn = new Thread(caption);
                threadcattn.Start();
                Thread threaddata = new Thread(data);
                threaddata.Start();
                if (textBox1.Text.Contains("youtube"))
                {
                    label5.Text = textBox1.Text.Substring(32);
                    string pic_url = "https://i.ytimg.com/vi/" + textBox1.Text.Substring(32) + "/mqdefault.jpg";
                    pictureBox1.LoadAsync(pic_url);
                }
                else
                {
                    Thread threadthux = new Thread(thdler);
                    threadthux.Start();
                }
            }
        }

        private void button2_Click_1(object sender, EventArgs e) //download
        {
            string vd = comboBox1.SelectedItem.ToString();
            string ad = comboBox2.SelectedItem.ToString();
            string cap = comboBox3.SelectedItem.ToString();
            string ms = comboBox4.SelectedItem.ToString();
            string[] vx = vd.Split(' ');
            string[] ax = ad.Split(' ');
            string[] cx = cap.Split(' ');
            string User = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile).ToString();
            string Output = textBox4.Text.Replace(User, "");
            Output = Output.Replace("\\", "/");
            if (vx[0].Length == 10 && ax[0].Length==10 && cx[0].Length==10 && ms.Length==11)
            {
                MessageBox.Show("Select streams", "ytdl", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else if (vx[0].Length != 10 && ax[0].Length != 10 && cx[0].Length == 10 && ms.Length == 11)
            {
                string Arg = "--add-metadata --no-mtime --no-restrict-filenames -o " + "\"~" + Output + "%(title)s.%(ext)s\" -f " + vx[0] + "+" + ax[0] + " " + textBox1.Text;
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (vx[0].Length != 10 && ax[0].Length != 10 && cx[0].Length != 10 && ms.Length == 11)
            {
                string Arg = "--add-metadata --no-mtime --write-srt --sub-lang "+cx[0]+" --embed-subs -o " + "\"~" + Output + "%(title)s.%(ext)s\" -f " + vx[0] + "+" + ax[0] + " " + textBox1.Text;
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (ms.Contains("MP3 64K Low music") && vx[0].Length == 10 && ax[0].Length == 10 && cx[0].Length == 10)
            {
                string Arg = "--add-metadata --no-mtime -x --audio-format mp3 --audio-quality 64K -o " + "\"~" + Output + "%(title)s.%(ext)s\"  " + textBox1.Text;
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (ms.Contains("MP3 320K High music") && vx[0].Length == 10 && ax[0].Length == 10 && cx[0].Length == 10)
            {
                string Arg = " --add-metadata --no-mtime -o " + "\"~" + Output + "%(title)s.%(ext)s\"  "+" -x " + textBox1.Text+ " --audio-format mp3 --audio-quality 320K  --add-metadata --embed-thumbnail";
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (ms.Contains("M4A High music") && vx[0].Length == 10 && ax[0].Length == 10 && cx[0].Length == 10)
            {
                string Arg = " --no-mtime -o " + "\"~" + Output + "%(title)s.%(ext)s\"  " + " -x " + textBox1.Text + " --audio-format m4a --add-metadata --embed-thumbnail";
                label5.Text = Arg;
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (ms.Contains("WAV High music") && vx[0].Length == 10 && ax[0].Length == 10 && cx[0].Length == 10)
            {
                string Arg = "  --add-metadata --no-mtime -o " + "\"~" + Output + "%(title)s.%(ext)s\"  " + " -x " + textBox1.Text + " --audio-format wav   --add-metadata --embed-thumbnail";
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }
            else if (ms.Contains("FLAC 24 bit Studio music") && vx[0].Length == 10 && ax[0].Length == 10 && cx[0].Length == 10)
            {
                string Arg = " --add-metadata --no-mtime -o " + "\"~" + Output + "%(title)s.%(ext)s\"  " + " -x " + textBox1.Text + " --audio-format flac   --add-metadata --embed-thumbnail";
                Thread childThreadx = new Thread(() => progress(Arg));
                childThreadx.Start();
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            using (var fbd = new FolderBrowserDialog())
            {
                DialogResult result = fbd.ShowDialog();
                if (result == DialogResult.OK && !string.IsNullOrWhiteSpace(fbd.SelectedPath))
                {
                    string[] files = Directory.GetFiles(fbd.SelectedPath);
                    textBox4.Text = fbd.SelectedPath;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            textBox1.Text = Clipboard.GetText();
        }

        private void rjButton1_Click(object sender, EventArgs e)
        {
            button1_Click(sender, e);
        }

        private void rjButton1_Click_1(object sender, EventArgs e)
        {
            button5_Click(sender, e);
        }
    }
}
