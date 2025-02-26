"use client";

import { cn } from "@/lib/style";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { useActionState, useEffect, useState } from "react";
import { useToast } from "@/hooks/use-toast";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { createAction } from "@/server-actions/chatbot-message/create";
import { Settings, X, ImagePlus, SendHorizonal, FileText } from "lucide-react"
import { parseFilesToBase64, Base64File } from "@/lib/parse-file";

type Props = {
	chatbotId: string;
	className?: string;
};

export const CreateChatbotMessageForm = ({ chatbotId, className }: Props) => {
	const router = useRouter();
	const { toast } = useToast();
	const [images, setImages] = useState<Base64File[]>([]);
	const [docs, setDocs] = useState<Base64File[]>([]);

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			chatbotId: chatbotId,
			resource: "openai",
			mode: "discussion",
			prompt: "",
			images: [],
			docs: []
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Message Successfully",
			});
			router.refresh();
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Message",
			});
		}
	}, [state]);

	const handleImageChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
		const selected = e.target.files;
		if (!selected) return; // null チェック
		const parsed = await parseFilesToBase64(selected)
		setImages((prev) => [...prev, ...parsed]);
	};

	const handleRemoveImage = (index: number) => {
		setImages((prev) => prev.filter((_, i) => i !== index));
	};

	const handleDocsChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
		const selected = e.target.files;
		if (!selected) return; // null チェック
		const parsed = await parseFilesToBase64(selected)
		setDocs((prev) => [...prev, ...parsed]);
	};

	const handleRemoveDoc = (index: number) => {
		setDocs((prev) => prev.filter((_, i) => i !== index));
	};

	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		const formData = new FormData(e.currentTarget);
	
		// 画像ファイルを追加
		if (images.length > 0) {
			Array.from(images).forEach((image) => formData.append("images", image.base64));
		}

		// 書類ファイルを追加
		if (docs.length > 0) {
			Array.from(docs).forEach((doc) => formData.append("docs", doc.base64));
		}
	
		formAction(formData);
	};

	return (
		<form
			onSubmit={handleSubmit}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader className={'flex flex-row items-center justify-between'}>
					<CardTitle>Chat with AI</CardTitle>
					<DropdownMenu>
						<DropdownMenuTrigger asChild>
							<Button type="button" variant="outline" size="icon">
								<Settings size={24} />
							</Button>
						</DropdownMenuTrigger>
						<DropdownMenuContent align="end" className={"flex flex-col gap-2 p-2"}>
							<DropdownMenuItem className={"w-full"} asChild>
								<Label className={'flex justify-between gap-1.5'}>
									LLM
									<Select
										key={state.inputs?.resource}
										name={"inputs.resource"}
										defaultValue={state.inputs?.resource}
									>
										<SelectTrigger className="w-[120px]">
											<SelectValue />
										</SelectTrigger>
										<SelectContent>
											<SelectItem value="openai">OpenAI</SelectItem>
											<SelectItem value="google">Google</SelectItem>
											<SelectItem value="anthropic">Anthropic</SelectItem>
										</SelectContent>
									</Select>
								</Label>
							</DropdownMenuItem>
							<DropdownMenuItem className={"w-full"} asChild>
								<Label className={'flex gap-1.5'}>
									Mode
									<Select
										key={state.inputs?.mode}
										name={"inputs.mode"}
										defaultValue={state.inputs?.mode}
									>
										<SelectTrigger className="w-[120px]">
											<SelectValue placeholder="Mode" />
										</SelectTrigger>
										<SelectContent>
											<SelectItem value="discussion">Discussion</SelectItem>
											<SelectItem value="code">Code</SelectItem>
											<SelectItem value="prompt" disabled>
												Prompt
											</SelectItem>
											<SelectItem value="summary" disabled>
												Summary
											</SelectItem>
											<SelectItem value="translation" disabled>
												Translation
											</SelectItem>
										</SelectContent>
									</Select>
								</Label>
							</DropdownMenuItem>
						</DropdownMenuContent>
					</DropdownMenu>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Input
						type={"hidden"}
						key={state.inputs?.chatbotId}
						name={"inputs.chatbotId"}
						defaultValue={state.inputs?.chatbotId}
					/>
					<Label className={'flex flex-col gap-1.5'}>
						<Textarea
							className={"resize-none h-full border-0 focus-visible:ring-0"}
							autoFocus
							key={state.inputs?.prompt}
							name={"inputs.prompt"}
							defaultValue={state.inputs?.prompt}
							placeholder={"Ask AI anything..."}
						/>
						{state.validationErrors?.prompt && (
							<small className={"px-2"}>{state.validationErrors?.prompt}</small>
						)}
					</Label>


					{/* 画像プレビューエリア */}
					{images.length > 0 && (
						<div className="flex flex-wrap gap-2">
						{images.map((image, index) => {
							return (
								<div key={index} className="relative w-24 h-24">
									{/* プレビュー画像 */}
									<Image
										src={`data:${image.type};base64,${image.base64}`}
										alt={image.name}
										fill
										className="object-cover rounded-md" />

									{/* 削除ボタン（左上） */}
									<Button
										type="button"
										variant={"ghost"}
										size={"icon"}
										onClick={() => handleRemoveImage(index)}
										className="w-5 h-5 absolute -top-2 -left-2 rounded-full bg-slate-700/70"
									>
										<X size={16} />
									</Button>
								</div>
							);
						})}
						</div>
					)}

					{/* 書類プレビューエリア */}
					{docs.length > 0 && (
						<div className="flex flex-wrap gap-2">
						{docs.map((doc, index) => {
							return (
								<div key={index} className="relative flex items-center gap-2 p-2 bg-gray-100 rounded-md">
									<span className="text-sm text-gray-600">{doc.name}</span>
									<Button
										type="button"
										variant={"ghost"}
										size={"icon"}
										onClick={() => handleRemoveDoc(index)}
										className="w-5 h-5 absolute -top-2 -left-2 rounded-full bg-slate-700/70"
									>
										<X size={16} />
									</Button>
								</div>
							);
						})}
						</div>
					)}

					<div className="flex justify-between items-center w-full mt-2 px-2">
						{/* 添付ボタン（左下） */}
						<div className={"flex items-center gap-1.5"}>
							{/* Image */}
							<div>
								<Input
									type="file"
									accept="image/*"
									multiple
									onChange={handleImageChange}
									id="image-upload"
									className="hidden"
								/>
								<Button
									type="button"
									variant="outline"
									size="icon"
									onClick={() => document.getElementById("image-upload")?.click()}
								>
									<ImagePlus size={24} />
								</Button>
							</div>
							{/* Docs */}
							<div>
								<Input
									type="file"
									accept=".pdf,.md"
									multiple
									onChange={handleDocsChange}
									id="docs-upload"
									className="hidden"
								/>
								<Button
									type="button"
									variant="outline"
									size="icon"
									onClick={() => document.getElementById("docs-upload")?.click()}
								>
									<FileText size={24} />
								</Button>
							</div>
						</div>

						{/* 送信ボタン（右下） */}
						<Button type="submit" size="icon" disabled={isPending}>
							<SendHorizonal size={24} />
						</Button>
					</div>
				</CardContent>
			</Card>
		</form>
	);
};
