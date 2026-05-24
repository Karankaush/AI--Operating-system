"use client"

import { uploadPdf } from "@/services/pdf.service"
import { useRef } from "react"

import { Upload } from "lucide-react"

import { Button } from "@/components/ui/button"


export default function PdfUpload() {

  const inputRef =
    useRef<HTMLInputElement | null>(null)


  const handleButtonClick = () => {

    inputRef.current?.click()
  }


  const handleFileChange = async (
  event: React.ChangeEvent<HTMLInputElement>
) => {

  const file = event.target.files?.[0]

  if (!file) return

  try {

    const response = await uploadPdf(file)

    console.log(response)

  } catch (error) {

    console.log(error)
  }
}


  return (
    <div className="border-b border-zinc-800 p-4">

      <input
        type="file"
        accept=".pdf"
        ref={inputRef}
        className="hidden"
        onChange={handleFileChange}
      />

      <Button
        onClick={handleButtonClick}
        className="
          w-full
          gap-2
          bg-blue-600
          text-white
          hover:bg-blue-700
        "
      >
        <Upload className="h-4 w-4" />

        Upload PDF

      </Button>

    </div>
  )
}